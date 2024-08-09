from django.shortcuts import render
from django.views import View

from .models import AllUser

# Create your views here.
common_data = {
    'username': 'user_name',
    'useremail': 'user_email'
}

class AddUser(View):
    def get(self, request):
        common_data['form_action'] = f'{self.request.build_absolute_uri('/')}user/verify_added_user/'
        print("common_data['form_action']:::::", common_data['form_action'])
        return render(request, 'htmls/users_add_user.html', common_data)
    
    # def post(self, request):
    #     common_data['form_action'] = f'{self.request.build_absolute_uri('/')}user/verify_added_user/'
    #     print("common_data['form_action']:::::", common_data['form_action'])
    #     return render(request, 'htmls/users_add_user.html', common_data)

    
class VerifyAddedUser(View):
    def post(self, request):
        user_name = self.request.POST
        print('user_name:::::', user_name.get(common_data['username']))
        return render(request, 'htmls/users_verify_added_user.html', common_data)
    
