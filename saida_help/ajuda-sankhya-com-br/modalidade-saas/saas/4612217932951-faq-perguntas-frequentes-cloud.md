---
id: "4612217932951"
titulo: "FAQ - Perguntas Frequentes - CLOUD"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4612217932951-FAQ-Perguntas-Frequentes-CLOUD"
trilha: "Modalidade SaaS > SaaS"
atualizado_em: "2026-07-22T15:18:46Z"
rotulos: ["Segurança", "Segurança escalabilidade e backups automáticos", "Acesso ao BD restrito; suporte 24x7", "Sem limite de armazenamento; boa conexão necessária", "Infraestrutura", "Suporte", "Saas", "Backup", "Cloud"]
---

# FAQ - Perguntas Frequentes - CLOUD

**Quais as principais vantagens do Cloud?**

Conectividade, elasticidade, monitoramento e otimização, atualizações automáticas da infraestrutura interna, segurança, backup armazenado em regiões diferentes, implantação rápida e ágil, acesso à tecnologias atualizadas e inovadoras, deixando o ambiente mais seguro, pois o ambiente local caso não seja bem gerenciado é mais vulnerável.

**Como faço para acessar o meu BD direto? E se eu precisar de um backup ou fazer um update em um registro no banco?**

O acesso ao banco não é permitido devido a questões de segurança dos dados. Caso seja necessário qualquer intervenção via banco, o cloud irá analisar a viabilidade para aprovar e executar. Quando solicitado pelo cliente, o link para baixar o backup é enviado em até 24 horas, e fica disponível por 15 dias.

**Utilizo banco de dados SQL, quero mudar para nuvem mantendo o mesmo banco de dados. É possível?**

Como consumimos serviços da Oracle, não é possível o cliente hospedar no Sankhya Cloud fazendo uso do banco SQL. Para este caso, será necessário a conversão do SQL para Oracle. Atualmente a Sankhya não presta este serviço, porém existem no mercado empresas que dão esse suporte. Só será migrado o banco local para a nuvem após a conversão para o banco de dados Oracle.

**Minha operação é 24X7, como funciona o suporte do Cloud? Se meu sistema parar às 23:00hr no domingo que é meu momento de pico, o que fazer?**

Não temos operação de suporte para isso. Porém, temos monitoramento 24x7 para atuarmos de forma preventiva e proativa caso ocorra algum incidente.

**Qual espaço disponibilizado na nuvem?**

Não tem limite de armazenamento, e sim quantidade de usuários. Um dos serviços do Cloud Sankhya é a realização de tuning periodicamente para garantir uma performance adequada de acordo com o volume de dados e usuários, para que a performance seja a mais eficiente possível.

**Quais os canais de atendimento Cloud?**

Os mesmos canais de atendimento Sankhya pois o ambiente é de responsabilidade Sankhya: Voip, e-mail, telefone, chat da plataforma.

**Não é necessário investimento algum na minha infraestrutura, pois eu vou precisar apenas de um link para acesso à internet. Essa afirmação é correta?**

Se tratando de servidor para banco de dados e aplicação não será necessário investimento em infra. Portanto continua sendo de suma importância estações de trabalho para os usuários com as configurações adequadas, e uma boa internet, com possível redundância caso tenha muita oscilação. Na minuta do contrato, é possível encontrar as recomendações para a estação de trabalho.

**Atualmente utilizo Tableau, e gostaria de manter como minha principal ferramenta de BI, é possível?**

Caso a ferramenta seja da Sankhya teremos que analisar as necessidades da mesma para integração com nosso ambiente. Se não for da sankhya a princípio não podemos por questões de segurança (Acesso externo ao banco de dados por terceiros), exceto se a ferramenta for via API, neste caso, seria possível.

**Atualmente tenho contrato com uma empresa que cuida do meu servidor de BD e das soluções de apoio a gestão Tableau e Yanmar, uma vez hospedando com vocês, este atendimento também está previsto no contrato?**

Não damos suporte à ferramentas terceiras e o Tableau ou quaisquer outras ferramentas de BI que fazem conexão com o banco de dados, não são suportadas. Mas podem ser utilizados o dashboard e/ou a ferramenta de BI da própria Sankhya.

**Como faço para acessar o sistema se eu estiver hospedado no Cloud e ficar sem internet?**

Não consegue acessar, pois é necessário conexão com Internet.

**Porque não posso ter acesso ao Banco de Dados?**

Por questões de segurança. No nosso modelo de serviço SaaS, toda a administração do ambiente é feita pela equipe da Sankhya, com isso não efetuamos liberação do acesso ao banco para garantir a integridade das informações e limitar o risco de qualquer alteração prejudicial que possa ocorrer no mesmo, visto que para isso teríamos que liberar acesso externo. Porém existe uma tela dentro do sistema chamada DBExplorer, no qual é possível efetuar consultas diretas no banco de dados.

**Esse ambiente suporta quantos usuários?**

Em termos de Infraestrutura não temos um limite devido a liberdade de poder mexer nos nodes e apps para alocar maior espaço. Porém ai vai de caso em caso, pois quanto maior quantidade de clientes mais recursos computacionais teremos que alocar na infra, portanto,  de alguma forma isso terá de ser repassado ao cliente, e repassado a equipe técnica na hora de fazer a criação da aplicação para garantir que a aplicação seja criada com os recursos necessários.

**Para acessar o Sankhya Om fora do domínio da minha empresa, é preciso estar no Cloud da Sankhya?**

No Sankhya Cloud, ou em qualquer outro provedor de Cloud.

**Tenho dentro do grupo de empresas um varejo de autopeças, consigo ter o PDV off-line funcionando na nuvem?**

Sim, o PDV é um "ponto de venda" instalado em cada máquina (local) que for utilizá-lo. Durante a instalação, é criado (automaticamente) um banco de dados local - o que permite posterior sincronização com o ERP, quando a conexão e/ou o ERP ficar disponível novamente.

**O ambiente Sankhya Cloud é exclusivo da minha empresa?**

O ambiente Sankhya Cloud funciona como se fosse um navio de containers. O navio seria o banco de dados inteiro, que comporta vários outros bancos dentro dele (estes "outros bancos" seriam os containers lacrados). Dessa forma, apesar de terem vários clientes no mesmo banco, o ambiente de cada parceiro é isolado, ou seja, as informações não se misturam.
