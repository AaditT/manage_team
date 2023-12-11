from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import TeamMember
from .forms import AddTeamMemberForm, UpdateTeamMemberForm
from django.views.decorators.http import require_POST

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
            return render(request, 'add_teammember.html', {'form': form})
    else:
        form = AddTeamMemberForm()
    return render(request, 'add_teammember.html', {'form': form})

def update_teammember(request, id):
    teammember = TeamMember.objects.get(id=id)
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'delete':
            teammember.delete()
            return redirect('teammembers')
        else:
            form = UpdateTeamMemberForm(request.POST, instance=teammember)
            if form.is_valid():
                form.save()
                return redirect('teammembers')
            else:
                return HttpResponse("Invalid form data")
    else:
        form = UpdateTeamMemberForm(instance=teammember)
    return render(
        request, 'update_teammember.html', 
        {
            'form': form,
            'teammember': teammember
        }
    )

@require_POST
def delete_teammember(request, id):
    teammember = TeamMember.objects.get(id=id)
    teammember.delete()
    return redirect('teammembers')