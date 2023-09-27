# AWS cli

Instalar cliente de consola:

  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  unzip awscliv2.zip
  sudo ./aws/install

Configurar region por defecto:

  Para que el cli de aws tome region por defecto se debe de crear una carpeta .aws y dentro colocar un archivo llamado config sin extension con el siguiente contenido:

  [default]
  region = eu-west-1
  output = json

Crear credenciales en AWS para acceder a los recursos:

Se debe ingresar en IAM > Usuarios y crearlo, una vez creado mostrara un api id key y un access key

Almacenar credenciales

Para que el cli de aws tome un perfil por defecto con sus credenciales se debe de crear una carpeta .aws y dentro colocar un archivo llamado credentials sin extension con el siguiente formato:

  [default]
  aws_access_key_id = XXXXXXXXXXXX
  aws_secret_access_key = XXXXXXXXXXXX

Tambien es posible añadir varios perfiles si es necesario en el mismo archivo. Para cambiar entre perfiles se usa el siguiente comando:

  aws --profile my-profile

Conectar con cluster:

  aws eks update-kubeconfig --name arya-digital --region eu-west-1 --profile arya-prod
