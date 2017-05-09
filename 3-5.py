#3-5 Changing Guest List

guest_list = ['Jesus', 'Oprah', 'Obamas', 'Ethel Little']
print("Thank you so much for coming, " + guest_list[0] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[1] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[2] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[3] + "! It means so much to me!")
print("Oh no, so sorry that the " + guest_list[2] + " can't make it:(")

guest_list.remove('Obamas')
guest_list.append('Beyonce')
print("Thank you so much for coming, " + guest_list[0] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[1] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[2] + "! It means so much to me!")
print("Thank you so much for coming, " + guest_list[3] + "! It means so much to me!")