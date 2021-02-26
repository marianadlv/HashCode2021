from instapy import InstaPy

insta_username = 'yukidlv'
insta_password = 'jumcyv-vypgo9-Wazwur'

session = InstaPy(username=insta_username, password=insta_password)
session.login()

session.set_do_comment(enabled=True, percentage=100)
session.set_comments(["@nataliaarandam"])
#https://www.instagram.com/p/CLnEeKpnGB9/

session.interact_by_URL(urls=["https://www.instagram.com/p/B6ocXt9Jp6GuiOmGta3gy3rpLKkEILGA9j5t_c0/"], randomize=True, interact=True)

session.end()
