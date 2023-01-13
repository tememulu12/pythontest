from survey import AnonymousSurvey

question = 'Jaki jest Twój język native?'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('Wpisz q aby zakończyć.')
while True:
    response = input('Język: ')
    if response == 'q':
        break
    my_survey.store_response(response)
print('Dziękujemy za udzielenie odpowiedzi')
my_survey.show_results()
