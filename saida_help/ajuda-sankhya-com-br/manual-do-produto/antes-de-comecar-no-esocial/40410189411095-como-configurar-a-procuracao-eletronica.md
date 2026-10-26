---
id: "40410189411095"
titulo: "Como configurar a procuração eletrônica e a assinatura digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40410189411095-Como-configurar-a-procura%C3%A7%C3%A3o-eletr%C3%B4nica-e-a-assinatura-digital"
trilha: "Manual do Produto > Pessoas+ > eSocial > Antes de Começar no eSocial"
atualizado_em: "2026-10-02T15:57:11Z"
rotulos: ["Configuração", "eSocial", "Central do eSocial", "Certificado digital", "Erro", "Procuração Eletrônica e Assinatura Digital para o eSocial", "411 - Assinante inválido", "Procuração Eletrônica"]
---

# Como configurar a procuração eletrônica e a assinatura digital

O governo disponibiliza orientações oficiais para configuração de assinatura digital e procuração eletrônica:

[Orientações sobre assinatura digital e procuração eletrônica no eSocial](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/orientacoes-assinatura-digital-e-procuracao-eletronica?utm_source=chatgpt.com)

Nesse material, consulte especialmente:

- Configuração de procuração eletrônica;
- Definição de representantes;
- Permissões de transmissão;
- Procedimento no e-CAC para definição dos perfis para procuração.

#### **(3)**Erro 411 no eSocial: Assinante inválido

O erro **411 - Assinante inválido** ocorre quando o certificado digital utilizado no envio dos eventos ao eSocial não possui permissão para transmitir informações em nome da empresa, ou quando existem inconsistências relacionadas ao certificado digital e à procuração eletrônica.

Esse erro normalmente está relacionado a:

- certificado digital vencido;
- procuração eletrônica vencida;
- certificado incorreto;
- ausência de procuração para o transmissor;
- inconsistências entre matriz e filial;
- instabilidade temporária no ambiente do eSocial.

A mensagem pode ocorrer durante o envio de eventos pela **Central do eSocial** no Pessoal+:

- Eventos de Tabela (S-1000 a S-1070);
- Eventos Não Periódicos (S-2200 a S-2300);
- Eventos Periódicos (S-1200 a S-1299);
- Eventos de SST (S-2210 a S-2240).

**Exemplo comum de cenário**

Uma empresa utiliza o certificado digital do escritório contábil para transmitir os eventos do eSocial.

A procuração eletrônica vence e não é renovada.

Ao tentar enviar os eventos pela Central do eSocial no Sankhya, o governo retorna:

> 411 - Assinante inválido

Nesse caso, basta renovar a procuração eletrônica e aguardar a atualização no ambiente do governo.

#### Principais causas do erro

#### 1. Certificado digital vencido

Quando o certificado digital da empresa ou do contador está vencido, o eSocial bloqueia a assinatura dos eventos.

**Como validar no Sankhya**

- Acesse a tela **Empresas** (Pessoal+ » Cadastros » Empresas);
- Na aba **Certificado Digital**, verifique:

  - certificado selecionado;
  - validade do certificado;
  - caminho do arquivo.

    ![Imagem 1: caminho do arquivo.](https://ajuda.sankhya.com.br/hc/article_attachments/40410189410071)

Se estiver vencido:

1. Clique em **Importar certificados do sanesocial**;
2. Escolha um certificado válido;
3. Salve o cadastro;
4. Retorne à **Central do eSocial** e retransmita os eventos.

#### 2. Procuração eletrônica vencida ou inexistente

Quando os eventos são enviados utilizando o certificado do contador ou de terceiros, é obrigatório existir uma procuração eletrônica válida no eCAC/eSocial.

⚠️ Sem procuração válida, o eSocial rejeita os eventos com erro de assinante inválido.

**O que validar**

- se a procuração está ativa;
- se foi emitida para o CNPJ correto;
- se contempla os serviços do eSocial;
- se ainda está dentro da validade.

⚠️ Empresas matriz e filial podem exigir procurações individuais para cada CNPJ.

Após criar uma nova procuração, o governo pode levar algumas horas para disponibilizar a autorização.

#### 3. Certificado digital incorreto

O erro também pode ocorrer quando:

- o certificado informado no sistema não corresponde ao transmissor;
- o caminho do certificado está incorreto;
- existe troca entre certificado de matriz e filial.

**Validações recomendadas**

Confira:

- se o certificado pertence ao CNPJ correto;
- se a inscrição do transmissor está correta;
- se o certificado configurado no Sankhya é o mesmo utilizado no eCAC.

#### 4. Problemas de matriz e filial

Em empresas com matriz e filial:

- o certificado da filial só pode ser utilizado para a própria filial;
- recomenda-se priorizar o certificado da matriz para evitar inconsistências.

Além disso:

- cada filial pode exigir procuração própria;
- o CNPJ utilizado no envio deve corresponder ao certificado configurado.

#### 5. Instabilidade no ambiente do eSocial

Em alguns casos, o erro ocorre devido a indisponibilidade temporária dos serviços do governo.

Quando todas as configurações estiverem corretas:

1. aguarde alguns minutos;
2. tente retransmitir os eventos;
3. acompanhe o status do eSocial.

Se o problema persistir, entre em contato com o suporte oficial do eSocial.

### **(3)**Recomendações gerais

Antes de retransmitir os eventos:

- valide o certificado digital;
- revise a procuração eletrônica;
- confira o CNPJ transmissor;
- valide matriz e filial;
- confirme a validade do certificado;
- teste novamente o envio.
