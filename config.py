class Configuration:

  def get_configuration(choose):

    if(choose == 'local'):
      connect_value = dict(host='HOSTNAME',
        user='USERID',
        password='PASSWORD',
        database='DBNAME',
        port=3307,
        charset='utf8')
      
    elif(choose == 'ubuntu'):
      connect_value = dict(host='HOSTNAME',
        user='USERID',
        password='PASSWORD',
        database='DBNAME',
        port=3307,
        charset='utf8')

    else:
      print('Not Selected')
      connect_value = ''

    return connect_value

  def get_token(choose):

    telegram = {
        'BOTNAME':['-XXXXXXXXXXXXXX','XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXX'],
    } 

    if(choose == 'telegram'):
      value = telegram.get('BOTNAME')    
    else:
      print('Not Selected')
      value = ''

    return value    
  