'''__init__.py 裡面放package所需的function
    可以import檔案名稱或直接寫在裡面
    這是一命名空間

'''

from .postg import get_cites,is_email_duplicate,add_user
from . import postg

