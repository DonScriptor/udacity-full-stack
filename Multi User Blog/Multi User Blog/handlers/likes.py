"""
Handles likes post request and also error handlings of those cases
"""
from google.appengine.ext import db

from entities.entity import Post, User, Like
from handlers.auth import AuthHandler

from datetime import datetime


class LikeBlog(AuthHandler):
    """

    """
    def get(self, post_id):
        """
        """
        user_obj = User.get_by_id(int(self.user))
        if not self.user:
            cookie_error = "Your session has expired please login again to continue!"
            self.render('login.html', error=cookie_error)
        else:
            post = Post.get_by_id(int(post_id))
            author = post.user.key().id()
            import pdb; pdb.set_trace()
            if author == int(self.user) or Like.all().filter('post =', post).filter('user =', user_obj).get() != None:
                self.redirect('/like/error')
            else:
                like = Like(post=post, user=user_obj)
                like.put()
                self.redirect("/blog/{}".format(post.slug))
