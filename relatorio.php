<?php
// Configurações do banco de dados
$servername = "localhost";
$username = "seu_usuario";
$password = "sua_senha";
$dbname = "seu_banco_de_dados";

// Criar conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificar conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Consulta SQL para selecionar usuários
$sql = "SELECT id, login, senha, telefone, email,  created_at FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Saída dos dados de cada linha
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Username</th><th>Email</th><th>Created At</th></tr>";
    while($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row["id"]. "</td><td>" . $row["login"]. "</td><td>" . $row["senha"]. "</td><td>" . $row["telefone"]. "</td><td>" . $row["email"]. "</td><td>" .
        $row["created_at"]. "</td></tr>";
    }
    echo "</table>";
} else {
    echo "0 resultados";
}
$conn->close();
?>


Lista de cadastros (LUCAS) 

<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="">
<title>Lista De Cadastros</title>
</head>
<body>
<table border="2">
    <tr>
        <th>Id</th>
        <th>Login</th>
        <th>Senha</th>
        <th>Telefone</th>
        <th>E-mail</th>
    </tr>
  
    <tr>
        <td> <?php echo $_rows["id"];?> </td>
        <td> <?php echo $_rows["Login"];?> </td>
        <td> <?php echo $_rows["senha"];?> </td>
        <td> <?php echo $_rows["telefone"];?> </td>
        <td> <?php echo $_rows["email"];?> </td>
       
     <td>   <a href="">Editar</a>  </td>
     <td>    <a href="">Alterar</a>  </td>
    </td>    
    </tr>
    
</table>
