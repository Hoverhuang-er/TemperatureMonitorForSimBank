from pydrive import GoogleAuth
from pydrive import GoogleDrive
class DriveSaver:
    def __init__(self):
        self.drive = None
        try:
            gauth = GoogleAuth()
            
            gauth.LoadCredentialsFile("celsius_degree ()")
            gauth.LoadCredentialsFile("dust ()")
            gauth.LoadCredentialsFile("humidity ()")
            if gauth.credentials is None:
                
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
            
                gauth.Refresh()
            else:
               
                gauth.Authorize()
           
            gauth.SaveCredentialsFile("celsius_degree ()")
            gauth.SaveCredentialsFile("dust ()")
            gauth.SaveCredentialsFile("humidity ()")
            self.drive = GoogleDrive(gauth)
        except:
            gauth = GoogleAuth()
            gauth.LocalWebserverAuth()
            self.drive = GoogleDrive(gauth)


    def save(self, filename):
        try:
            file5 = self.drive.CreateFile()
            file5.SetContentFile(filename) 
            file5.Upload() 
        except:
            print ("Faile")

    def listFiles(self):
        file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in file_list:
            print 'title: %s, id: %s' % (file1['title'], file1['id'])

def main():
    d = DriveSaver()
    d.listFiles()

if __name__ == "__main__": main()
