# AWS cli

Instalar cliente de consola:

  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  
  unzip awscliv2.zip
  
  sudo ./aws/install

Configurar region por defecto:

  Para que el cli de aws tome region por defecto se debe de crear una carpeta .aws y dentro colocar un archivo llamado config sin extension.
  
  mkdir .aws  
  
  nano .aws/config
  
Añadimos este contenido al archivo config:

  [default]
  region = eu-west-1
  output = json


Crear credenciales en AWS para acceder a los recursos:

Se debe ingresar en IAM > Usuarios y crearlo, una vez creado mostrara un api id key y un access key

Almacenar credenciales

Para que el cli de aws tome un perfil por defecto con sus credenciales se debe de crear una carpeta .aws y dentro colocar un archivo llamado credentials sin extension

  nano .aws/credentials

Con el siguiente contenido:

  [default]
  aws_access_key_id = XXXXXXXXXXXX
  aws_secret_access_key = XXXXXXXXXXXX

Tambien es posible añadir varios perfiles si es necesario en el mismo archivo. Para cambiar entre perfiles se usa el siguiente comando:

  aws --profile my-profile


eksctl create iamidentitymapping   --cluster arya-digital   --region eu-west-1   --arn "arn:aws:iam::234366607644:role/AWSReservedSSO_AdministratorAccess_54f908375f73549c"   --username "{{SessionName}}"   --group "system:masters"   --profile arya-dev

Conectar con cluster:

  aws eks update-kubeconfig --name arya-digital --region eu-west-1 --profile arya-prod


Comando para añadir usuarios federados al cluster role via consola:

eksctl create iamidentitymapping \
  --cluster aggraria \
  --region eu-west-1 \
  --arn "arn:aws:iam::996152156047:role/AWSReservedSSO_AdministratorAccess_25d86d2cb8454820" \
  --username "{{SessionName}}" \
  --profile aggraria \
  --group "system:masters"

# ECR

Subir imagen a ECR de forma manual:

Nota: usar root y configurar el perfil por default usando el comando aws configure

Hacer login:

  aws ecr get-login-password --region eu-west-1 --profile default | docker login --username AWS --password-stdin 234366607644.dkr.ecr.eu-west-1.amazonaws.com/keycloak-dev

Contruir imagen:

  docker build --platform linux/amd64 -t 234366607644.dkr.ecr.eu-west-1.amazonaws.com/keycloak-dev:latest --build-arg CI_COMMIT_REF_NAME=dev .

Subir imagen:

  docker push 234366607644.dkr.ecr.eu-west-1.amazonaws.com/keycloak-dev:latest




