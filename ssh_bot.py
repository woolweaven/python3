import getpass                                                                                        
import paramiko                                                                                       
                                                                                                      
class Client:                                                                                         
    def __init__(self, ipaddr, user, passwd):                                                         
        self.ipaddr = ipaddr                                                                          
        self.user = user                                                                              
        self.passwd = passwd                                                                          
                                                                                                      
    def ssh_connect(self):                                                                            
        try:                                                                                          
            client = paramiko.SSHClient()                                                             
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())                              
            client.load_system_host_keys()                                                            
            client.connect(hostname = self.ipaddr, username = self.user,password =  self.passwd)      
            stdin, stdout, stderr = client.exec_command('ls -lah')                                    
            print(stdout.readlines())                                                                 
            #return client                                                                            
                                                                                                      
        except Exception as e:                                                                        
            print('Operation error: %s' % e)                                                          
                                                                                                      
newClient = Client(input('Remote IP: '), input('Username: '), getpass.getpass('Password: '))          
newClient.ssh_connect() 
