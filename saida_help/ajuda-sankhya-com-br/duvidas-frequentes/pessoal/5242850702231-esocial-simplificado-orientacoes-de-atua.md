---
id: "5242850702231"
titulo: "ESocial simplificado - Orientações de atualização"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5242850702231-ESocial-simplificado-Orienta%C3%A7%C3%B5es-de-atualiza%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:30:06Z"
rotulos: ["Produtos", "Configuração", "Central de Vendas", "Atualização", "#validadoRayssa", "eSocial", "Baixe descompacte execute com comandos específicos", "Passos simples para substituir e configurar", "Evite novos cadastros até atualização oficial"]
---

# ESocial simplificado - Orientações de atualização

Para a virada da versão é necessário a atualização do Sanesocial que é idêntico ao processo atual da versão 3.0, não há modificação da forma de uso, apenas uma atualização de versão do mesmo, não sendo necessária uma configuração diferente das que já existem no ambiente configurado.

| **Atenção**  Instalações:  a) A versão atual (3.1) do SaneSocial deve substituir a versão anterior ( 3.0), caso seja SO- Linux, a pasta do saneSocial anterior (3.0) deve ser excluída.  B) Após a instalação deve ser configurado como de costume o certificado e banco de dados. |
| --- |

Versões disponíveis no site de download da Sankhya: [Download](http://downloads.sankhya.com.br/downloads?app=SanESocial)

![Imagem 1: Inicie a instalação com modo administrador selecionado;](https://ajuda.sankhya.com.br/hc/article_attachments/16415020887575) Inicie a instalação com **modo administrador** selecionado;

![Imagem 2: Inicie a instalação com modo administrador selecionado;](https://ajuda.sankhya.com.br/hc/article_attachments/16415032789271)

![Imagem 3: Avance a primeira tela da instalação para selecionar a pasta na qual o serviço será instalado;](https://ajuda.sankhya.com.br/hc/article_attachments/16415020894103) Avance a primeira tela da instalação para selecionar a pasta na qual o serviço será instalado;

![Imagem 4: Avance a primeira tela da instalação para selecionar a pasta na qual o serviço será instalado;](https://ajuda.sankhya.com.br/hc/article_attachments/5242747473687)

![Imagem 5: Avance a seleção da pasta e também a seleção do nome do atalho no Menu Iniciar;](https://ajuda.sankhya.com.br/hc/article_attachments/16415032795415) Avance a seleção da pasta e também a seleção do nome do atalho no Menu Iniciar;

![Imagem 6: Avance a seleção da pasta e também a seleção do nome do atalho no Menu Iniciar;](https://ajuda.sankhya.com.br/hc/article_attachments/5242838292119)

![Imagem 7: Após avançar as opções definidas anteriormente, pode-se escolher se o serviço do San eSocial irá ou não iniciar…](https://ajuda.sankhya.com.br/hc/article_attachments/16415020897303) Após avançar as opções definidas anteriormente, pode-se escolher se o serviço do San eSocial irá ou não iniciar juntamente com o windows. Após avançar este passo o San eSocial será instalado, finalizando o carregamento pode-se passar para a configuração do serviço.

![Imagem 8: Após avançar as opções definidas anteriormente, pode-se escolher se o serviço do San eSocial irá ou não iniciar…](https://ajuda.sankhya.com.br/hc/article_attachments/5242751258263)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Link para dowload: [Sanesocial Linux](http://downloads.sankhya.com.br/downloads?app=SanESocial&c=1)

A instalação do San eSocial em ambiente **linux** segue os passos descritos abaixo:

![Imagem 9: Baixe o arquivo tar.gz do sanesocial e transfira para o servidor linux. Lembrando que, só será possível descompactá-lo…](https://ajuda.sankhya.com.br/hc/article_attachments/16415020887575) Baixe o  arquivo **tar.gz** do sanesocial e transfira para o servidor linux. Lembrando que, só será possível descompactá-lo com o usuário utilizado nesta transferência. Geralmente este usuário é o mgeweb ou root. No exemplo abaixo, foi utilizado o usuário mgeweb pelo aplicativo Winscp.

![Imagem 10: Baixe o arquivo tar.gz do sanesocial e transfira para o servidor linux. Lembrando que, só será possível descompactá-lo…](https://ajuda.sankhya.com.br/hc/article_attachments/5242815324823)

![Imagem 11: Após transferir o arquivo para o servidor linux, acesse pelo putty o diretório para o qual ele foi transferido. Aqui…](https://ajuda.sankhya.com.br/hc/article_attachments/16415020894103) Após transferir o arquivo para o servidor linux, acesse pelo putty o diretório para o qual ele foi transferido. Aqui ele está na pasta /home/mgeweb, e o nome do arquivo baixado é: sanesocial\_unixx64\_Sankhya\_2\_0b92.tar.gz.

![Imagem 12: Após transferir o arquivo para o servidor linux, acesse pelo putty o diretório para o qual ele foi transferido. Aqui…](https://ajuda.sankhya.com.br/hc/article_attachments/5242816865431)

![Imagem 13: Execute o comando: tar -xzvf sanesocial_unixx64_Sankhya_2_0b92.tar.gz e assim será exibido na tela que ele foi…](https://ajuda.sankhya.com.br/hc/article_attachments/16415032795415)  Execute o comando: tar -xzvf sanesocial\_unixx64\_Sankhya\_2\_0b92.tar.gz e assim será exibido na tela que ele foi descompactado.

![Imagem 14: Execute o comando: tar -xzvf sanesocial_unixx64_Sankhya_2_0b92.tar.gz e assim será exibido na tela que ele foi…](https://ajuda.sankhya.com.br/hc/article_attachments/5242915317271)

![Imagem 15: Feito isto, neste mesmo diretório será apresentada uma pasta chamada sanesocial, acesse-a com: cd sanesocial . Execute…](https://ajuda.sankhya.com.br/hc/article_attachments/16415020897303) Feito isto, neste mesmo diretório será apresentada uma pasta chamada sanesocial, acesse-a com: cd sanesocial. Execute o comando de listagem de arquivos neste diretório com ls e inicie a aplicação com nohup ./sanesocial.sh > /dev/null &

![Imagem 16: Feito isto, neste mesmo diretório será apresentada uma pasta chamada sanesocial, acesse-a com: cd sanesocial . Execute…](https://ajuda.sankhya.com.br/hc/article_attachments/5242922216343)

![Imagem 17: Acesse o console da aplicação no navegador com: ip_do_servidor:8778/index.html](https://ajuda.sankhya.com.br/hc/article_attachments/16415241296023) Acesse o console da aplicação no navegador com: ip\_do\_servidor:8778/index.html

![Imagem 18: Acesse o console da aplicação no navegador com: ip_do_servidor:8778/index.html](https://ajuda.sankhya.com.br/hc/article_attachments/5242842205463)

![Imagem 19: Atualize os scripts;](https://ajuda.sankhya.com.br/hc/article_attachments/16415241297047) Atualize os scripts; 

![Imagem 20: Atualize os scripts;](https://ajuda.sankhya.com.br/hc/article_attachments/16415346012055)

**![Imagem 21: ATENÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16415329556119) ATENÇÃO:**

Nas versões 4.9 e 4.10 do MGE Pessoal e MGE Ponto e no Pessoal+ acima das versões 4.9b234 e 4.10b140 foram disponibilizadas opções no cadastro de horário de trabalho, que **ainda não devem ser utilizadas no layout atual 2.5 do eSocial, que é o disponível para as transmissões.**

**Portanto, caso haja o cadastro de novo horário de trabalho, não efetue nenhum registro nos campos;**

**Observação:** necessário que o parâmetro **"USAESOCIALSIMPL"** esteja ativo.

**Tipo de Jornada:**

Correspondente ao campo eSocial: tpJornada (Tipo de jornada)

2 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso)

3 - Jornada com horário diário fixo e folga variável

4 - Jornada com horário diário fixo e folga fixa (no domingo)

5 - Jornada com horário diário fixo e folga fixa (exceto no domingo)

6 - Jornada com horário diário fixo e folga fixa (em outro dia da semana), com folga adicional periódica no domingo

7 - Turno ininterrupto de revezamento

9 - Demais tipos de jornada

**Possui Horário Noturno (total ou parcial)**

Correspondente ao campo eSocial: horNoturno (indica se a jornada semanal possui horário noturno: todo ou em parte).

**MGE Pessoal » Arquivos » Cadastros » Carga Horária**

![Imagem 22: MGE Pessoal » Arquivos » Cadastros » Carga Horária](https://ajuda.sankhya.com.br/hc/article_attachments/16415346014615)

**Pessoal+ » Cadastros » Carga Horária**

![Imagem 23: Pessoal+ » Cadastros » Carga Horária](https://ajuda.sankhya.com.br/hc/article_attachments/12387080994455)

**Essas opções se aplicam para a versão da Simplificação 1.0.** Portanto, podem gerar incidentes durante a transmissão na versão atual, devido às novas parametrizações.

Para mais informações consulte o [Manual de Orientação do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-0-consolidada-ate-a-no-s-1-0-09-2021.pdf)

**Importante:** será encaminhado um novo comunicado a partir do momento que todos puderem realizar a virada da chave e efetivar as adequações necessárias para atender o layout da Simplificação do eSocial versão S-1.0.

#### Para mais informações, acesse o artigo: [Portaria Conjunta SEPRT/RFB nº 82](https://ajuda.sankhya.com.br/hc/pt-br/articles/5428090623511)
