---
id: "32151650076183"
titulo: "Sankhya - Autenticação de dois fatores 2FA"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32151650076183-Sankhya-Autentica%C3%A7%C3%A3o-de-dois-fatores-2FA"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-24T12:42:35Z"
rotulos: ["Usuários", "Segurança", "SMTP", "Autenticação", "Token", "Sankhya ID", "Controle de Acesso", "Parâmetro", "Autenticação de dois fatore", "2FA"]
---

# Sankhya - Autenticação de dois fatores 2FA

A plataforma já possui diversos **recursos de segurança** que, aliados às **boas práticas de segurança** corporativa, auxiliam o Administrador do Sistema a **manter a integridade de seu ambiente**.
Mas, sempre pensando na segurança e compliance, **foi adicionada uma camada extra de segurança no processo de identificação do usuário, o 2FA ou Autenticação em Dois Fatores**. O que significa que o usuário deverá comprovar sua identidade de duas maneiras diferentes antes que o acesso ao sistema seja concedido. O primeiro fator é o convencional, informando usuário e senha e, após o sucesso desta etapa, o segundo fator será a inserção de um token enviado para o e-mail informado no cadastro deste usuário.

**Veja abaixo como acontecerá o acesso tendo a autenticação em dois fatores:**

![Imagem 1: Faça login normal com usuário e senha:](https://ajuda.sankhya.com.br/hc/article_attachments/32151650060183) Faça login normal com usuário e senha:

![Imagem 2: Faça login normal com usuário e senha:](https://ajuda.sankhya.com.br/hc/article_attachments/32151682114455)

![Imagem 3: Tendo sucesso desta etapa, uma tela será aberta para o usuário que está logando informar o token recebido no seu e-mail…](https://ajuda.sankhya.com.br/hc/article_attachments/32151650062743) Tendo sucesso desta etapa, uma tela será aberta para o usuário que está logando informar o token recebido no seu e-mail de usuário ou reenviar o mesmo:

![Imagem 4: Tendo sucesso desta etapa, uma tela será aberta para o usuário que está logando informar o token recebido no seu e-mail…](https://ajuda.sankhya.com.br/hc/article_attachments/32151682115351)

![Imagem 5: Token recebido para o usuário atual:](https://ajuda.sankhya.com.br/hc/article_attachments/32151650064023) Token recebido para o usuário atual:

![Imagem 6: Token recebido para o usuário atual:](https://ajuda.sankhya.com.br/hc/article_attachments/32151682116375)

![Imagem 7: Após informar o token e clicar em continuar, será realizada abertura da home page do sankhyaOM:](https://ajuda.sankhya.com.br/hc/article_attachments/32151682116759) Após informar o token e clicar em continuar, será realizada abertura da home page do sankhyaOM:

![Imagem 8: Após informar o token e clicar em continuar, será realizada abertura da home page do sankhyaOM:](https://ajuda.sankhya.com.br/hc/article_attachments/32151650068119)

### Como habilitar e configurar a 2FA

A habilitação desse recurso de segurança adicional é realizada via argumentos do servidor, ou seja via configuração do servidor. Para termos a rotina funcional é importante:

- Ter o servidor SMTP configurado na tela Servidor SMTP;
- Ter uma boa gestão sobre os e-mails de usuários do sistema, que realmente estão informados e atualizados.

![Imagem 9: A configuração -Dsnk.2fa.level pode ser feita com uma das seguintes opções ou múltiplas separadas por vírgula: none,…](https://ajuda.sankhya.com.br/hc/article_attachments/32151650060183) A configuração **-Dsnk.2fa.level** **pode ser feita** com uma das seguintes **opções ou múltiplas** separadas por vírgula: **none, all, high ou admin**. Veja detalhes abaixo:

(1)** none:** não utiliza (que pode ser usado para desabilitar temporariamente a rotina, isso se for deixado apenas a opção none, na configuração);

(1)** all:** ativação da autenticação 2FA para todos os usuários;

(1)** high:** usuários que tenham acesso a no mínimo uma das telas da lista abaixo:
Construtor de Telas
Construtor de componentes de BI
DBExplorer
Dicionário de dados
Relatórios formatados;
Extrator de dados;
Ações agendadas
Módulo Java
Editor de Variáveis
Construtor de DashBoard

(1)** admin:** Apenas para usuários considerados Admin como Sup, Sankhya, Jiva e Consultor. Como estes usuários não se destinam a uma pessoa em específico, eles utilizam uma configuração de e-mail diferente, conforme os detalhes abaixo:

**(2)N e-mails devem ser configurados no seguinte arquivo:** **“/home/mgeweb/sankhyaconf/[BASE]/admin/mail.cfg”;**

**(2)**Cada um dos e-mails listados no arquivo descrito acima, receberão o token no caso de acesso, porém com a identificação do usuário ao qual o token pertence. **Exemplo:**

**(3)**Digamos que no arquivo “mail.cfg” tenha os seguintes e-mails: [sup@sankhya.com.br;](mailto:sup@sankhya.com.br;) [consultor@sankhya.com.br;](mailto:consultor@sankhya.com.br;) 
**(3)**Se o usuário Consultor logar no sistema, os dois e-mail do item anterior receberão o token informando que pertence ao usuário Consultor, e este deve ser informado para que o acesso seja concluído;

**Observação importante:** ao ativar o 2FA, usuários administradores como o SUP são automaticamente incluídos no processo de autenticação. Este é um comportamento padrão do sistema, não podendo ser alterado, pois são usuários com maior nível de acesso e exigem maior controle de segurança.

![Imagem 10: Exemplo de uso: Dsnk.2fa.level=all Dsnk.2fa.level=all,high](https://ajuda.sankhya.com.br/hc/article_attachments/32151650062743) **Exemplo de uso:**
**(1)** Dsnk.2fa.level=all
**(1)** Dsnk.2fa.level=all,high

![Imagem 11: Além da configuração principal -Dsnk.2fa.level, existem duas configurações adicionais que permitem um controle mais…](https://ajuda.sankhya.com.br/hc/article_attachments/32151650064023) Além da configuração principal -Dsnk.2fa.level, existem duas **configurações adicionais que permitem um controle mais refinado da autenticação em dois fatores**, possibilitando definir usuários ou grupos específicos que deverão utilizar o 2FA.

**(1)** -**Dsnk.2fa.ulist** equivale a um ou uma lista de usuários, separados por vírgula, que terão a autenticação de dois fatores, utilizando o e-mail configurado no cadastro de cada um destes usuários.
Exemplos:
-Dsnk.2fa.ulist=1
-Dsnk.2fa.ulist=3,4

**(1)** -**Dsnk.2fa.glist:** segue a mesma descrição da configuração anterior, porém o controle é feito por Grupo de Usuários, permitindo informar um ou mais grupos, separados por vírgula.
Exemplos:
-Dsnk.2fa.glist=1
-Dsnk.2fa.glist=7,8,15

**Observação Importante:**

As configurações adicionais **-Dsnk.2fa.ulist e -Dsnk.2fa.glist são dependentes da configuração principal -Dsnk.2fa.level.** Ou seja, p**ara que seja possível definir usuários ou grupos específicos, é imprescindível que o parâmetro -Dsnk.2fa.level esteja previamente configurado.**

**Quando utilizadas em conjunto, as configurações adicionais se sobressaem à regra geral definida no -Dsnk.2fa.level**, permitindo um controle mais específico sobre quem deverá utilizar a autenticação em dois fatores.

Exemplo:
-Dsnk.2fa.level=all
-Dsnk.2fa.ulist=1

Neste cenário, a autenticação em dois fatores será exigida apenas para o usuário 1 e para o usuário SUP, que possui obrigatoriedade nativa de utilização do 2FA.

![Imagem 12: Validade ou expiração do token Pensando em trazer flexibilização para a implantação e utilização da 2FA, principalmente…](https://ajuda.sankhya.com.br/hc/article_attachments/32151682116759) **Validade ou expiração do token**
Pensando em trazer flexibilização para a implantação e utilização da 2FA, principalmente durante o período de adaptação dos usuários, foram disponibilizadas algumas opções de expiração para o token. Por padrão a validade é de 12 horas, no entanto, é possível alterar este comportamento através da configuração do servidor **-Dsnk.2fa.timeout**, que pode ser definido como descrito abaixo:

**(1)** **Dsnk.2fa.timeout=8H:** é possível realizar o tempo de validade do token em horas, onde o mínimo é de 1 hora e o máximo de 72 horas;
**(1)** **Dsnk.2fa.timeout=2D:** a segunda possibilidade é em dias, onde o mínimo é de 1 dia e o máximo é de 3 dias;

Caso o usuário tenha realizado o **acesso ao Sankhya, com um token válido, os demais acessos deste mesmo usuário só irão solicitar um novo token se expirar a validade** definida no argumento: Dsnk.2fa.timeout=8H ou **se acontecer** uma das **exceções** abaixo:

**(1)**Caso o servidor do **SankhyaOM seja reiniciado**, todos os token expiram automaticamente e os novos acessos seguiram o processo de informar um token válido;
**(1)** Caso um **segundo acesso seja realizado utilizando um browser diferente**, um novo token será solicitado ao usuário, e o processo segue normalmente. Um exemplo é quando o usuário acessa utilizando o navegador Sankhya, e faz um segundo acesso utilizando o Chrome.
**(1)** Caso um **segundo acesso seja realizado utilizando um endereço de IP de uma rede diferente**, um novo token será solicitado ao usuário, e o processo segue normalmente. Um exemplo é se o usuário acessar o sistema via a rede da empresa e, em um outro momento, realizar um segundo acesso da sua rede residencial.

Disponível à partir das versões:

4.21b191
4.22b238
4.23b216
4.24b139
4.25b84
4.26 qualquer build.
