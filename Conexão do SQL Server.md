Conexão do SQL Server



Aqui mostrarei os passos que fiz para conseguir fazer a conexão



Primeiro tenha instalado:

 	SQL SERVER 2022 -> [Link Download](https://info.microsoft.com/ww-landing-sql-server-2022.html?lcid=pt-br)

 	SSMS 21 -> [Link Download](https://aka.ms/ssms/21/release/vs_SSMS.exe)

 	Alguma ferramenta de banco de dados ex: Dbeaver



✅ 1. Verifique se o serviço do SQL Server está ativo

Pressione Win + R e digite:



&nbsp;	*services.msc*



Procure por um serviço chamado algo como:



SQL Server (MSSQLSERVER01)



Verifique se ele está com o status "Em execução".



Se não estiver, clique com o botão direito e selecione Iniciar.



✅ 2. Permitir conexões TCP/IP no SQL Server

Abra o SQL Server Configuration Manager (pesquise no menu iniciar).



Vá em:



SQL Server Network Configuration > Protocols for MSSQLSERVER01

Ative o protocolo TCP/IP (se estiver desativado).



Clique com o botão direito > Enable.



Clique com o botão direito em TCP/IP > Propriedades.



Vá na aba IP Addresses, desça até IPAll, e veja se a porta TCP está definida como 1433.



📌 Se não estiver, adicione 1433 no campo TCP Port (não no TCP Dynamic Port).



Clique em OK e reinicie o serviço SQL Server.



✅ 3. Usar a conexão correta no DBeaver

No DBeaver, use:



Host:

127.0.0.1



Porta:

1433



Database:

master (ou outro, se tiver criado)



Authentication:

Windows Authentication (Trusted Connection)



✅ 4. Liberar a porta 1433 no firewall do Windows

Vá em Painel de Controle > Sistema e Segurança > Firewall do Windows.



Clique em Configurações avançadas.



Vá em Regras de Entrada > Nova Regra.



Tipo: Porta.



Protocolo: TCP, porta específica: 1433.



Permitir conexão.



Nomeie como “SQL Server 1433” e conclua.



🚀 Depois disso

Reinicie o SQL Server, depois reinicie o DBeaver e tente conectar de novo.



Se ainda assim não funcionar, me envie:



O host/porta que você está colocando



Se a instância MSSQLSERVER01 está “em execução”



E se o TCP/IP está habilitado





❌Caso der erro de certificado
SOLUÇÃO MAIS PRÁTICA: Usar localhost no lugar de 127.0.0.1,1433

Volte para o SSMS.



Em Server Name, digite:



localhost\\MSSQLSERVER01

Mantenha "Autenticação do Windows".



Marque "Confiar no certificado do servidor".



Clique em Conectar.



Por que isso funciona?

Quando você usa 127.0.0.1,1433, o SQL Server tenta autenticar via TCP/IP direto e entra em conflito com o SPN (Service Principal Name).



Já localhost\\INSTANCIA usa nome local nomeado, que evita o erro de SPPI e Kerberos.



✅ Alternativa definitiva: Criar login sa e usar autenticação SQL

Como sua intenção final é usar o DBeaver com o login sa, o caminho mais robusto e livre de dores é:



Entrar no SSMS com:



localhost\\MSSQLSERVER01

Ativar o sa, definir senha.



Mudar no DBeaver para usar SQL Server Authentication.



Se der certo com localhost\\MSSQLSERVER01, me avisa que eu continuo com o passo seguinte: ativar o login sa e configurar o SQL Server pro DBeaver.





✅ Habilitar o login sa e permitir autenticação por usuário e senha

🔧 1. Ativar autenticação mista (Windows + SQL Server)

No SSMS, clique com o botão direito sobre o nome do servidor no canto esquerdo (ex: PEDRINHO-PC\\MSSQLSERVER01)



Vá em Propriedades



Vá até a aba Segurança (Security)



Marque a opção:

✅ SQL Server e autenticação do Windows



Clique em OK



🔧 2. Ativar o login sa e definir senha

No painel esquerdo, expanda:





Segurança > Logins

Clique com o botão direito em sa > Propriedades



Aba Geral:



Defina uma senha forte (anote)



Aba Status:



Em "Login": selecione Habilitado



Clique em OK



🔁 3. Reinicie o SQL Server

Feche o SSMS.



Abra o services.msc



Reinicie o serviço:



SQL Server (MSSQLSERVER01)

🔌 4. Conecte no DBeaver com sa

Abra o DBeaver e edite ou crie nova conexão:



Campo	Valor

Host	127.0.0.1

Porta	1433

Database	master

Autenticação	SQL Server Authentication

Usuário	sa

Senha	(a que você acabou de definir)



✅ Marque: "Confiar no certificado do servidor" se necessário



Clique em Testar conexão — deve funcionar agora 100%!

