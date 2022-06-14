#
# This module is to create email template.
#

# import win32com.client as win32 
# def Emailer(text, subject, recipient):
#     outlook = win32.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.To = recipient
#     mail.Subject = subject
#     mail.HtmlBody = text
#     # mail.send