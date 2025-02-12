$date = Get-Date -Format "dd-MM-yyyy hh:mm:ss"
$logpath = "c:\AllUsersOpera.log"
Set-Content -Path $logpath -Value "$date Inicio de script"

# Crear el directorio C:\Windows\Sun\Java\Deployment si no existe
$destinationPath = "C:\Windows\Sun\Java\Deployment"
if (-Not (Test-Path -Path $destinationPath)) {
    Add-Content -Path $logpath -Value "Creando carpeta de deployment"
    New-Item -Path $destinationPath -ItemType Directory -Force
}

Add-Content -Path $logpath -Value "Inicio de copia de ficheros"
# Copiar los archivos desde "Java Exceptions" a "C:\Windows\Sun\Java\Deployment"
$sourcePath = "Java_Exceptions"
if(-Not(Test-Path -Path $sourcePath)){
    Add-Content -Path $logpath -Value "No se puede acceder a $sourcePath"
}
try {
    Copy-Item -Path "$sourcePath\deployment.config" -Destination $destinationPath -Force
    Copy-Item -Path "$sourcePath\deployment.properties" -Destination $destinationPath -Force
    Copy-Item -Path "$sourcePath\exception.sites" -Destination $destinationPath -Force

    Add-Content -Path $logpath -Value "Java files copiados correctamente"
}
catch {
    Add-Content -Path $logpath -Value "No se han podido copiar los java files"
}
