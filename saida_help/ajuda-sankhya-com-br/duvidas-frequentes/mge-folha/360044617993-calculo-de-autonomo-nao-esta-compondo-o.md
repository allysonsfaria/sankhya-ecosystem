---
id: "360044617993"
titulo: "Cálculo de autônomo não está compondo o valor da parte empresa na GPS. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044617993-C%C3%A1lculo-de-aut%C3%B4nomo-n%C3%A3o-est%C3%A1-compondo-o-valor-da-parte-empresa-na-GPS-Como-resolver"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:33:52Z"
rotulos: ["#criadoRoger", "Configuração", "Eventos", "Impostos", "Folha", "GPS", "Autônomo", "Autônomo excluído da GPS", "Informações incorretas no cadastro", "Corrigir eventos e bases"]
---

# Cálculo de autônomo não está compondo o valor da parte empresa na GPS. Como resolver?

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16979895592599) SITUAÇÃO:**

Cálculo de autônomo não está compondo o valor da parte empresa na GPS.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16979865620759)SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: MGEPessoal » Menu » Arquivos » Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/16979865621527) Acesse: MGEPessoal » Menu » Arquivos » Eventos

- Eventos: 4 - HONORARIOS PREST SERV e 5 - HONORARIOS TRANSP RODOV: verifique a informação do campo **"Identificação do Evento"= 119 - Evento Honorários;**

- Evento: 910 - INSS - HONORARIOS PREST SERV: verifique a informação do campo **"Identificação do Evento"**= **109 - Evento INSS Honorários Prestação de Serviços;**

- Evento: 911 - INSS - HONORARIOS TRANSP RODOV: verifique a informação do campo **"Identificação do Evento"**= **111 - Evento INSS Honorários do Transporte Rodoviário;**

![Imagem 4: Acesse: MGEPessoal » Menu » Arquivos » Bases de Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/16979865623319) Acesse: MGEPessoal » Menu » Arquivos » Bases de Cálculo

- Bases: 1910 - BASE INSS HONOR PREST SERV: verifique a informação do campo **"Identificação da Base"**= **18 - Base INSS Honorários Prestadores de Serviços**

- Bases: 1911 - BASE INSS HONOR TRANSP RODOV: Verificar a informação do campo **"Identificação da Base"**= **19 - Base INSS Honorários do Transporte Rodoviário**

![Imagem 5: Acesse: MGEPessoal » Arquivos » Funcionários » Acessar o cadastro do Autônomo - aba 'Admissão' » aba 'Dados Gerais'](https://ajuda.sankhya.com.br/hc/article_attachments/16979895599767) Acesse: MGEPessoal » Arquivos » Funcionários » Acessar o cadastro do Autônomo - aba 'Admissão' » aba 'Dados Gerais'

- Verifique a informação do campo **"Vínculo"= 90 - Autônomo**
- Aba **"Dados p/ FGTS"** >> Verifique a informação do campo:

Se o Autônomo for **Prestador de Serviço:** 13 Contribuinte individual – Trabalhador autônomo ou a este equiparado, inclusive o operador de máquina, com contribuição sobre remuneração; trabalhador associado à cooperativa de produção

Se o Autônomo for **Transportador Rodoviário**: 15 Contribuinte individual – Transportador autônomo, com contribuição sobre remuneração

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16979895601943)CAUSA:**

Ocorre quando as identificações dos Eventos e Bases, que participam do cálculo dos Autônomos, não estão preenchidas ou não estão corretas. Outro motivo é quando o Vínculo no cadastro do Autônomo não está como '90' ou quando a Categoria do FGTS não está correta.
