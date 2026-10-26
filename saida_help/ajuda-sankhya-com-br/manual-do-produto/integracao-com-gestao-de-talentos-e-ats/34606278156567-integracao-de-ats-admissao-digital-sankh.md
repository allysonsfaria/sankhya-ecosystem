---
id: "34606278156567"
titulo: "Integração de ATS <> Admissão Digital Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya"
trilha: "Manual do Produto > Pessoas+ > Integrações do Ecossistema Sankhya RH > Integração com Gestão de Talentos e ATS"
atualizado_em: "2026-09-26T01:40:51Z"
rotulos: ["Configuração", "Integração", "Folha de Pagamento", "Mindsight", "Dados Integrados", "Integração de ATS", "Admissão Digital", "RH", "ATS"]
---

# Integração de ATS <> Admissão Digital Sankhya

**Versão Mínima:** Sankhya Om: **4.35** - Pessoal+: **5.42**

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K4SRKJVEWATT7Y2B4PMMSZKM)

1. [Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K4SRKJVKHEMHY31PCA80ABM3)
2. [Fluxo de integração entre os sistemas](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K42T265JTNCK4P71T5FXPCX7)
3. [Campos integrados com a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K45DD5QNYWNSNVAJAPD4N9TJ)
4. [Tabelas acessadas no Sankhya](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K42T4K0TFDX5FM4HCQJNE7KK)

[Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K48B41W5G4P4BTQ255G881GB)

1. [Configuração da vaga](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K48B41W5G4P4BTQ255G881GB)
2. [Contratação do candidato](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K42WV6DH1BV0QZN7EKCTBRF8)

[Pontos de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K4SRWJAD813MG9M048SEE1XK)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K4SS1BZ2EA77933AP1WWWE89)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/34606278156567-Integra%C3%A7%C3%A3o-de-ATS-Admiss%C3%A3o-Digital-Sankhya#h_01K4SR4W40K4SYMRH0YS684KD3)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

A integração entre o **ATS (Mindsight)** e a **Admissão Digital Sankhya** automatiza o processo de contratação, tornando-o totalmente digital. 

O RH abre a vaga no Sankhya Om, que é enviada ao ATS. Quando o candidato é aprovado, ele recebe um e-mail com link e senha para acessar o Portal RH e preencher o formulário de admissão online. Os dados retornam ao Sankhya Om para finalização da admissão.

### 2. Fluxo de integração entre os sistemas

1. **Configuração da vaga:** Sankhya Om → ATS
2. **Contratação de um candidato:** ATS → Sankhya Om

### 3. Campos integrados com a folha

Quando a integração está ativa, na criação/edição da vaga, os seguintes dados são sincronizados:

- empresa;
- cargo;
- departamento.

Essas informações são usadas para direcionar a alocação do novo colaborador. Se os campos não forem preenchidos na configuração da vaga, serão obrigatórios no momento da contratação.

Informações como **nome**, **e-mail**, **CPF** e **salário** do candidato são enviadas do ATS para o Sankhya no momento da contratação do candidato.

### 4. Tabelas acessadas no Sankhya

A integração faz requisições GET nas seguintes tabelas:

- TFPEMP (EmpresaPessoal);
  - Puxa informações da TSIEMP (Empresa).
- TFPCAR (Cargo);
- TFPDEP (Departamento).

A integração faz requisições POST na seguinte tabela:

- TFPREQADM (RequisicaoAdmissao).

## Jornada de uso

### 1. Configuração da vaga

Na página de criação/edição da vaga, além dos campos obrigatórios, deve-se preencher a **Empresa**, o **Cargo** e o **Departamento**.

Esses campos trazem os dados já existentes no sistema do cliente e permitem que o recrutador defina antecipadamente onde o novo colaborador será alocado. Quando o candidato atingir a etapa de **Contratado(a)**, essas informações são enviadas automaticamente para o **Sankhya Om**.

[GIF animado: Imagem 1: Esses campos trazem os dados já existentes no sistema do cliente e permitem que o recrutador defina antecipadamente…](https://ajuda.sankhya.com.br/hc/article_attachments/34607746877719)

Caso esses campos não sejam preenchidos na configuração da vaga, eles serão obrigatoriamente requeridos na etapa de contratação do candidato. 

### 2. Contratação do candidato

Ao mover o candidato para etapa de **Contratado(a)**, deve-se ativar a opção **"Enviar para o processo de admissão da Sankhya"**, assim, o modal se expandirá com os dados necessários para a integração:

- **Empresa, cargo e departamento**
- **E-mail e CPF do candidato**

Após **"Contratar e concluir a vaga"**, o sistema gera automaticamente uma **requisição de admissão** no Sankhya Om e tudo passa a acontecer através do sistema Sankhya.

O candidato recebe um e-mail para preencher o formulário de admissão, e os próximos passos ficam com o Departamento Pessoal no Sankhya, que valida os dados e confirma a admissão.

[GIF animado: Imagem 2: O candidato recebe um e-mail para preencher o formulário de admissão, e os próximos passos ficam com o Departamento…](https://ajuda.sankhya.com.br/hc/article_attachments/34608422328343)

Mesmo após a integração, os dados podem ser ajustados no Sankhya pelo DP.

## Pontos de atenção

- Os campos empresa, cargo e departamento devem ser preenchidos na configuração da vaga ou serão obrigatórios na contratação.
- O CPF do candidato é obrigatório para cadastro.
- O e-mail do candidato é usado para envio do formulário de admissão.
- A empresa, o cargo e o departamento são importantes para o fazer o direcionamento e alocação correta dessa contratação dentro do sistema de folha.

## FAQ – Dúvidas Frequentes

(1)** Quais dados são integrados na criação/edição da vaga?**

           Empresa, cargo e departamento.

(2)** Quais dados são enviados na contratação do candidato?**

           Nome, e-mail, CPF e salário.

(3)** O que fazer se o candidato não receber o e-mail de admissão digital?**

           Acesse **Fila** (Configurações > Avançado > Envio de Mensagens), procure pelo e-mail do candidato e verifique o **"Status"** do envio.

![Imagem 3: Acesse Fila (Configurações > Avançado > Envio de Mensagens), procure pelo e-mail do candidato e verifique o "Status" do…](https://ajuda.sankhya.com.br/hc/article_attachments/34610820458263)

        Se não foi enviado, revise a configuração **SMTP** (protocolo responsável pelo envio dos e-mails) e contate o Service Desk da Sankhya para que o problema possa ser resolvido.

        Se foi enviado, confirme o e-mail do candidato e peça para verificar a pasta de spam/lixo eletrônico. Se mesmo assim houver algum problema com o recebimento do e-mail, entre em contato com o Service Desk da Sankhya para resolver o problema.

(4)** Como corrigir link incorreto no e-mail?**

          Em alguns casos, é possível que o link do Portal RH esteja mal configurado no Sankhya, fazendo com que o candidato não consiga acessar o formulário de admissão digital recebido por e-mail.

          Para corrigir isso, acesse a tela **Preferências** (Configurações > Avançado) e procure pela chave ENDACESSEXTWGE.

          Configure o campo **"Texto"** com o link correto e salve.

[GIF animado: Imagem 4: Configure o campo "Texto" com o link correto e salve.](https://ajuda.sankhya.com.br/hc/article_attachments/34611297472407)

         O link deve ser o de acesso externo ao sistema. Links locais não funcionarão. Esse link geralmente pode ser encontrado na tela **Configurações Gateway** (Configurações > Avançado):

![Imagem 5: O link deve ser o de acesso externo ao sistema. Links locais não funcionarão. Esse link geralmente pode ser encontrado…](https://ajuda.sankhya.com.br/hc/article_attachments/34611369725463)

(5)** Como resolver problemas de conexão com o Gateway?**

É comum encontrarmos problemas de conexão à base do cliente via Gateway. Isso acontece porque esses clientes podem ter um firewall ou VPN impedindo nossas conexões. 

Se houver erro de conexão (time-out), configure o firewall para liberar os IPs abaixo:

144.22.228.211

144.22.217.141

👉 Mais detalhes: [Seção 5.1 - Inclusão de IP’s no Firewall devido chamada do Gateway](https://developer.sankhya.com.br/reference/como-iniciar-uma-integracao-com-a-sankhya#51-inclus%C3%A3o-de-ip%C2%B4s-no-firewall-devido-chamada-do-gateway)

## Artigos Relacionados

- [Requisição de Admissão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059085273-Requisi%C3%A7%C3%B5es#admissao)
- [Configuração Funcionários](https://ajuda.sankhya.com.br/hc/pt-br/articles/21069685487639)
- [Integração de Folha <> Gestão de Talentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/34631564024599)
- [Integração de ATS <> Vlow](https://ajuda.sankhya.com.br/hc/pt-br/articles/34613039791383)
