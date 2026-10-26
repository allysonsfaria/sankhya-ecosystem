---
id: "360058061213"
titulo: "FAQ - Lei Geral de Proteção de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058061213-FAQ-Lei-Geral-de-Prote%C3%A7%C3%A3o-de-Dados"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-09-17T16:24:42Z"
rotulos: ["Configuração", "Segurança", "LGPD", "FAQ - Lei Geral de Proteção de Dados", "Privacidade", "Anonimização"]
---

# FAQ - Lei Geral de Proteção de Dados

**(1)** A **Lei Geral de Proteção de Dados** (Lei 13.709/18) está sendo discutida e estudada pelos mais diversos profissionais de modo a compreender suas implicações e impactos no dia-a-dia das empresas.

**(1)** O Grupo Sankhya se coloca à disposição para auxiliar no entendimento das adequações à Lei Geral de Proteção de Dados realizadas em nossos processos internos de atendimento.

Nesse documento são abordadas as **dúvidas mais frequentes** relacionadas a esse assunto:

**![Imagem 1: A Sankhya disponibiliza algum script de criptografia de dados pessoais e sensíveis para o Banco de dados?…](https://ajuda.sankhya.com.br/hc/article_attachments/17270636848791) A Sankhya disponibiliza algum script de criptografia de dados pessoais e sensíveis para o Banco de dados? Principalmente visando a LGDP?**

- Não são disponibilizados script de criptografia de dados, o que é feito no sistema **SankhyaOm** é a **anonimização de dados pessoais** para que não seja perdido performance. Com isso, é atendida a Lei que pede que seja anonimizado e não criptografado.
- Referente ao suporte ao **SankhyaOm**, quando necessário disponibilização do banco de dados para simulação de erros, os dados pessoais e sensíveis são anonimizados para proteção dos mesmos.

**![Imagem 2: Caso a Sankhya não disponibilize algum script de criptografia, o cliente pode aplicar a criptografia das tabelas de…](https://ajuda.sankhya.com.br/hc/article_attachments/17270629516567) Caso a Sankhya não disponibilize algum script de criptografia, o cliente pode aplicar a criptografia das tabelas de dados pessoais no banco?**

- Se o cliente usar o **SankhyaOm** ele não precisa rodar o script de criptografia, ele deve somente ligar o parâmetro da LGPD dentro do sistema e os dados já vão aparecer anonimizados.

**![Imagem 3: Se o cliente puder fazer a criptografia, onde na aplicação colocaremos a chave para fazer a descriptografia?](https://ajuda.sankhya.com.br/hc/article_attachments/17270636853015) Se o cliente puder fazer a criptografia, onde na aplicação colocaremos a chave para fazer a descriptografia?**

- Não faremos a criptografia, pois a nossa solução já atende a LGPD com a anonimização.

**![Imagem 4: O que a Sankhya recomenda para seus clientes com relação a criptografia ou anonimização dos dados de parceiros, visto…](https://ajuda.sankhya.com.br/hc/article_attachments/17270629520023) O que a Sankhya recomenda para seus clientes com relação a criptografia ou anonimização dos dados de parceiros, visto que essa é uma das premissas da LGPD?**

- A criptografia não é premissa da LGPD, porque a criptografia é reversível. O sistema **SankhyaOm** está adequado porque anonimiza os dados dentro da aplicação, visto que o cliente configura os usuários que podem ver os dados pessoais  e os dados pessoais sensíveis.

![Imagem 5: Após a anonimização, é possível fazer a edição do registro que possui dados anonimizados? Caso o formulário tenha algum…](https://ajuda.sankhya.com.br/hc/article_attachments/17270629526551)**Após a anonimização, é possível fazer a edição do registro que possui dados anonimizados? Caso o formulário tenha algum campo anonimizado e o usuário precisar fazer a edição de outro campo não anonimizado, isso é possível?**

- Pode ser feita configuração do usuário ou grupo de usuários os quais os dados estão aparecendo anonimizados, para não aparecerem mais anonimizados, se isto fizer sentido para a empresa.

**![Imagem 6: Por qual motivo uma senha é solicitada ao fazer download do log do servidor quando o parâmetro de proteção de dados…](https://ajuda.sankhya.com.br/hc/article_attachments/17270636861847) Por qual motivo uma senha é solicitada ao fazer download do log do servidor quando o parâmetro de proteção de dados está ativo?**

- No log do servidor existem chances de informações pessoais e sensíveis serem encontradas, e ao baixar esse log serem expostas a terceiros de forma indevida. Com a inclusão da senha, só quem a tem poderá descompactar o zip e consultar o log, olhando as consultas e demais dados que lá estiverem.
- Vale ressaltar que essa senha só é pedida quando o parâmetro de proteção de dados estiver ligado.

**![Imagem 7: É possível remover os alertas de tarja amarela informativos da LGPD?](https://ajuda.sankhya.com.br/hc/article_attachments/17270636862487)  É possível remover os alertas de tarja amarela informativos da LGPD?**

- Existe a opção "Aceitar" no final do texto, uma vez que clicar nela a tarja não mais será exibida para aquele usuário nesta tela. Nas demais telas que possuem a tarja também será necessário dar o aceite.

![Imagem 8: O que devo fazer para conseguir ver um dado que está anonimizado?](https://ajuda.sankhya.com.br/hc/article_attachments/17270636863767) **O que devo fazer para conseguir ver um dado que está anonimizado?**

- Para visualizar dados pessoais ou sensíveis a configuração dessa exceção deve ser configurada pela equipe de acessos do cliente de acordo com as configurações do cliente.
- As exceções podem ser aplicadas especificamente no campo, por usuário ou por grupo. Veja mais detalhes das configurações no documento: [https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaprote%C3%A7%C3%A3odedados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597874-Usu%C3%A1rios#abaprote%C3%A7%C3%A3odedados%20)

![Imagem 9: A Empresa realiza testes de vulnerabilidades externas e internas pelo menos anualmente?](https://ajuda.sankhya.com.br/hc/article_attachments/17270636870039) **A  Empresa realiza testes de vulnerabilidades externas e internas pelo menos anualmente?**

- Nossa empresa mantém todos os softwares de plataforma que utiliza sempre atualizados em termos de patches de segurança, como por exemplo, o Wildfly Application Server.
- Considerando que nossos clientes utilizam ambientes próprios (on premise ou private cloud), os testes de segurança são realizados por time próprio do cliente, nos reportando eventuais falhas encontradas por conta da combinação com o resto do ambiente de execução. Nos casos em que a falha é em nível de código, a patche é realizada.

**![Imagem 10: Considerando possíveis falhas oriundas do desenvolvimento do software de processamento de dados, há medidas de…](https://ajuda.sankhya.com.br/hc/article_attachments/17270636872599) Considerando possíveis falhas oriundas do desenvolvimento do software de processamento de dados, há medidas de contingência contra?**

- Há medidas de contingência contra acessos não autorizados. O sistema possui política configurável de senhas (qtd de dígitos, números, letras, etc), intervalo de expiração de senha e logout automático por inatividade ou horário de expediente, vide documentação de operação e configuração do sistema.
- Existe também opção para acesso apenas em computadores autorizados, porém não há suporte a verificação de duas fases.

**![Imagem 11: A Sankhya realiza atualização do software regularmente e as comunica aos seus clientes, para prevenção e mitigação de…](https://ajuda.sankhya.com.br/hc/article_attachments/17270629549207) A Sankhya realiza atualização do software regularmente e as comunica aos seus clientes, para prevenção e mitigação de possíveis falhas do sistema relacionadas a segurança de dados pessoais?**

- A Sankhya possui um Release Plan com publicações de novas versões a cada 2 meses. Essas novas versões são compostas por melhorias diversas, novos módulos, novas features e atualizações fiscais/contábeis.
- Novas demandas são analisadas levando em consideração o produto e o posicionamento dele no mercado, não apenas ao interesse exclusivo do cliente. Para demandas exclusivas existem diversas formas de personalizações na própria ferramenta e uma rede de serviços terceirizados especializados em customizações.

![Imagem 12: Considerando a especificidade do serviço prestado, a empresa coleta dados pessoais para controle e avaliação do volume…](https://ajuda.sankhya.com.br/hc/article_attachments/17270636876311) **Considerando a especificidade do serviço prestado, a empresa coleta dados pessoais para controle e avaliação do volume de usuários processados no sistema em cada licença? Em caso positivo, por quanto tempo é feito o armazenamento destes dados e como ocorre seu descarte? Quais medidas de segurança da informação são empregadas no o ciclo de vida destes dados?**

- Em nossa nuvem de dados, o Sankhya HUB, não temos nenhum tipo de informação sensível, quer seja de pessoas naturais ou pessoas jurídicas e temos um controle interno rígido sobre tudo o que vai para esse ambiente.
- No caso de bases que são solicitadas para simulação de erros para correção, estas são anonimizada preservando a privacidade dos dados, somente em casos que estes dados são necessários para a simulação que não ocorre esta anonimização, porém há um controle mais rígido no acesso destas bases. O descarte destas bases é realizado após 7 dias de sua criação e é feito automaticamente para preservar a segurança das informações.
