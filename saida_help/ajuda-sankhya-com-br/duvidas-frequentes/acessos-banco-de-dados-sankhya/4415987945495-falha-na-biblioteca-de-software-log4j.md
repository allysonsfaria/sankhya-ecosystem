---
id: "4415987945495"
titulo: "Falha na biblioteca de software Log4j"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4415987945495-Falha-na-biblioteca-de-software-Log4j"
trilha: "Dúvidas Frequentes > Acessos/Banco de Dados - Sankhya"
atualizado_em: "2026-07-22T15:20:15Z"
rotulos: ["Segurança", "Atualização", "#validadoJoaogomes", "Falha na Biblioteca Log4j: Sankhya Om Protegido", "Falha na biblioteca Log4j Vulnerabilidade de segurança Proteção da plataforma Sankhya", "vulnerabilidade Log4j segurança", "Java", "Apache", "Log4j", "Vulnerabilidade"]
---

# Falha na biblioteca de software Log4j

| **Os recursos oficiais da plataforma Sankhya não são afetados pelas vulnerabilidades identificadas na biblioteca Log4J.** |
| --- |

#### **(1)** O que é a Log4j?

Está sendo divulgado pela mídia uma vulnerabilidade da biblioteca de software Log4j.  Explicando de uma forma mais simples, a Log4j é uma biblioteca do Apache que auxilia desenvolvedores a realizar o que é chamado de "logging", um processo que permite guardar registros de interações, envio de informações, processamento de dados e resultados de uma determinada ação.

O "logging" possibilita guardar esse registro para analisar o comportamento de uma aplicação ou acompanhar as mudanças feitas durante o desenvolvimento do programa. A Log4j tem uma série de funcionalidades para esse fim e é usada em aplicações Java, muito populares ao redor do mundo.

#### **(1)** Qual o problema?

Uma falha de segurança na biblioteca Log4j  foi divulgada recentemente. Essa vulnerabilidade pode ser explorada para conseguir acesso a partes críticas das aplicações e permite que códigos maliciosos sejam enviados ao servidor da aplicação. 

Especialistas em cibersegurança classificaram essa falha como gravíssima (fonte: [CVE-2021-44228 Detail](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)). Segundo um levantamento da Check Point, no Brasil, 59% das redes corporativas monitoradas foram impactadas por tentativas de explorar essa vulnerabilidade, nas últimas semanas (fonte: [The Numbers Behind Log4j Vulnerability CVE-2021-44228](https://blog.checkpoint.com/2021/12/13/the-numbers-behind-a-cyber-pandemic-detailed-dive/)).

###

#### **(1)** O Sankhya Om está protegido?

Sim, todos os recursos oficiais da plataforma Sankhya estão seguros.

Após a divulgação da vulnerabilidade, os especialistas da Sankhya analisaram todas as aplicações da plataforma Sankhya, incluindo o servidor de aplicação, e nenhuma possui a vulnerabilidade citada. Tanto as aplicações, quanto as versões de servidor de aplicação que adotamos, utilizam versões seguras do Log4j. 

#### **(1)** Atenção para customizações

Mesmo que as aplicações oficiais da plataforma Sankhya estejam protegidas, recomendamos que as customizações em módulo java e extensões sejam verificadas pelos seus autores. É necessário confirmar que as versões da biblioteca Log4j Core 2.0 até 2.16 não estão sendo utilizadas pelas customizações. Caso estejam, solicitamos a imediata atualização para a versão 2.17 ou a remoção da classe “JndiLookup.class” do pacote Log4j. Detalhes sobre o procedimento podem ser encontrados em [Apache Log4j](https://logging.apache.org/log4j/2.x/security.html?_fsi=bzTnRsUe). 

#### **(1)** Especificações

| **CVE** | **efeito** | **Plataforma Sankhya** |
| --- | --- | --- |
| [CVE-2021-44228](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228) | Código malicioso pode ser carregado a partir do LDAP | as aplicações da plataforma Sankhya não são afetadas por essa vulnerabilidade, pois não utilizam as  versões comprometidas do Log4J |
| [CVE-2021-4104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4104) | Código malicioso pode ser executado remotamente | as aplicações da plataforma Sankhya não são afetadas por essa vulnerabilidade, pois a vulnerabilidade está associada ao JMSAppender, que não é usado em nossas soluções |

Para tirar dúvidas sobre essa questão, acesse o post na [comunidade Sankhya Developer.](https://comunidade.sankhya.com.br/t/vulnerabilidade-log4j-pode-causar-problemas-criticos/2162?u=laiane_ribeiro)
