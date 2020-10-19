import sys
import praw
import mysql.connector
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent,
                     username=config.username,
                     password=config.password)


def get_post_info(pos):
    return {
        'title': pos.title, 'author': str(pos.author),'upvote_ratio': pos.upvote_ratio, 'id': pos.id
    }


def get_comment_info(com):
    return {
        'body': com.body, 'comment_id': com.id, 'parent_id': com.parent_id,
        'link_id': com.link_id, 'author': str(com.author), 'score': com.score
    }


sub = reddit.subreddit(sys.argv[1])
sub_class = sys.argv[2]
if sys.argv[3] == 'hot':
    iter = sub.hot(limit=1000)
else:
    iter = sub.new(limit=100)

try:
    connection = mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         port=config.port,
                                         password=config.password,
                                         database=config.database,
                                         auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    use_query = "USE Reddit"
    cursor.execute(use_query)

    i_p = 0
    i_c = 0
    for post in iter:
        info = get_post_info(post)
        to_add = [info['title'], info['author'], info['upvote_ratio'], info['id'], sub_class]
        insert_query = """
                                INSERT IGNORE INTO Posts 
                                VALUES (DEFAULT, %s, %s, %s, %s, %s)
                                """
        cursor.execute(insert_query, to_add)
        connection.commit()
        if i_p % 5 == 0:
            print(f"Completed {i_p} posts")
        i_p += 1

        try:
            for comment in post.comments:
                c_info = get_comment_info(comment)
                to_add = [c_info['body'], c_info['comment_id'], c_info['parent_id'], c_info['link_id'],
                          c_info['author'], c_info['score'], sub_class]
                insert_query = """
                                                INSERT IGNORE INTO Comments 
                                                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)
                                                """
                cursor.execute(insert_query, to_add)
                connection.commit()
                if i_c % 50 == 0 and i_c != 0:
                    print(f'Completed {i_c} comments')
                i_c += 1

        except AttributeError:
            continue


except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

