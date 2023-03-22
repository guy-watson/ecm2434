from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Question
from leaderboard.models import Score






from django.shortcuts import render, redirect

@login_required
def profile(request):
    # Retrieve a question
    question = Question.objects.get(id=1)  # replace 1 with the id of the question you want to retrieve

    # Render the profile template with the question object
    return render(request, 'ecm2434/Q1.html', {'question': question})



def answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        selected_answer = request.POST.get('answer')

        # Retrieve the question object
        question = Question.objects.get(id=question_id)

        # Check if the selected answer is correct
        if selected_answer == question.correct_answer:
            # If it's correct, award points to the user
            print('Correct answer!')

            # Check if the user already has a Score object
            user_score = Score.objects.filter(player=request.user).first()

            points_awarded = 10  # Set the number of points to be awarded

            if user_score:
                # If the user has a Score object, update their score
                user_score.score += points_awarded
                user_score.save()
            else:
                # If the user doesn't have a Score object, create one
                user_score = Score(player=request.user, score=points_awarded)
                user_score.save()

            return redirect('home')
        else:
            # If it's incorrect, redirect back to the profile page
            print('wrong answer!')
            return redirect('profile')
    else:
        # Handle the case where the user navigates to this URL directly
        # without submitting a form (e.g., redirect to the profile page)
        return redirect('profile')

