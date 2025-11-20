results = {}
submissions = {}
while True:
    command = input()

    if command == 'exam finished':
        break

    if 'banned' in command:
        username = command.split('-')[0]
        results.pop(username)
    else:
        username, language, points = command.split('-') 
        if language in submissions.keys():
            submissions[language] += 1
        else:
            submissions[language] = 1
        if username not in results.keys():
            results[username] = 0
        if results[username] < int(points):
            results[username] = int(points)

print('Results:')
for user, points in results.items():
    print(f'{user} | {points}')

print('Submissions:')
for language, submissions_count in submissions.items():
    print(f'{language} - {submissions_count}')