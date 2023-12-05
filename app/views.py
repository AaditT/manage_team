from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import TeamMember
from .forms import AddTeamMemberForm


# Create your views here.

def teammembers(request):
    teammembers = TeamMember.objects.all()
    template = loader.get_template('teammembers.html')
    context = {
        'teammembers': teammembers,
        'num': len(teammembers)
    }
    return HttpResponse(template.render(context, request))




def add_teammember(request):
    if request.method == 'POST':
        form = AddTeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teammembers')
        else:
            return HttpResponse("Invalid form data")
    else:
        form = AddTeamMemberForm()
    return render(request, 'add_teammember.html', {'form': form})