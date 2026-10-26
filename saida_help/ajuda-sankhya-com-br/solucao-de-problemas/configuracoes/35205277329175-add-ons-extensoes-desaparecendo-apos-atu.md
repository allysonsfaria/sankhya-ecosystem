---
id: "35205277329175"
titulo: "Add-ons/Extensões Desaparecendo Após Atualização do Sankhya Om via WPM"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35205277329175-Add-ons-Extens%C3%B5es-Desaparecendo-Ap%C3%B3s-Atualiza%C3%A7%C3%A3o-do-Sankhya-Om-via-WPM"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:25:46Z"
rotulos: ["Produtos", "Configuração", "Atualização", "WPM", "addon", "add-ons", "desaparece atualização", "Desaparece", "Add-on", "Sankhya Om"]
---

# Add-ons/Extensões Desaparecendo Após Atualização do Sankhya Om via WPM

**SITUAÇÃO:**

Ocorre ao instalar ou atualizar o **"Sankhya Om"** via **"WPM"**. Normalmente, isso acontece quando há mudança de ambiente sem a devida reconfiguração, impedindo o **"WPM"** de localizar corretamente os add-ons já existentes.

**SOLUÇÃO:**

**(1)**  **Verifique a versão do "Gerenciador de Pacotes"**

- Certifique-se de que o **"Gerenciador de Pacotes"** esteja na **versão mais recente**.
- Para realizar o download, acesse:
  [Download do Gerenciador de Pacotes](https://downloads.sankhya.com.br/downloads?app=instaladores&c=1)

**(2)**  **Atualize ou reconfigure o ambiente**

- Após atualizar o **"Gerenciador de Pacotes"**, siga a documentação de configuração do **"Sankhya Om"**:

  - [**"Ambiente Windows"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045695134-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Windows)
  - [**"Ambiente Linux"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045547894-Manual-de-Instala%C3%A7%C3%A3o-Sankhya-Om-em-Ambiente-Linux)

**Importante:** mesmo que o **"Gerenciador de Pacotes"** já esteja na versão mais recente, a **reconfiguração do ambiente** pode ser necessária.

**(3)**  **Confirme a localização das extensões**

- Após configurar ou reconfigurar o ambiente, verifique se as extensões estão instaladas no diretório correto;

**(4)**  **Finalize o processo de atualização**

- Caso tenha interrompido o processo antes de reinstalar as extensões, prossiga atualizando novamente o ambiente via **"WPM"**.
- Após a conclusão, as extensões serão restauradas e estarão disponíveis no **"Sankhya Om"**.

**CAUSA:**

O problema ocorre porque, durante a atualização do **"Sankhya Om"** via **"WPM"**, há substituição de diretórios e arquivos de configuração. Se o ambiente não for reconfigurado corretamente após a atualização, o **"WPM"** não reconhece o diretório das extensões, fazendo com que os add-ons instalados anteriormente **não sejam carregados**.
