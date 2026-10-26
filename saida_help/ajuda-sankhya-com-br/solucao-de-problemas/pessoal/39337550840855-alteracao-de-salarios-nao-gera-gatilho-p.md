---
id: "39337550840855"
titulo: "Alteração de Salários Não Gera Gatilho para Envio ao eSocial S-2206"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39337550840855-Altera%C3%A7%C3%A3o-de-Sal%C3%A1rios-N%C3%A3o-Gera-Gatilho-para-Envio-ao-eSocial-S-2206"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-18T11:10:33Z"
rotulos: ["Atualização", "Folha", "eSocial", "Configuração Funcionários", "Central do eSocial", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Alteração de Salários Não Gera Gatilho para Envio ao eSocial S-2206

**SITUAÇÃO**

Ao realizar **reajuste salarial** para colaboradores através da rotina específica de ajuste salarial ou aplicação de **Convenção Coletiva de Trabalho** (CCT), o evento **S-2206** (Alteração de Contrato de Trabalho) **não é gerado automaticamente** na **"Central de Eventos do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial). Essa situação impede o envio das alterações salariais ao eSocial, mesmo com os valores corretos registrados no cadastro do funcionário.

**SOLUÇÃO**

Para resolver o problema de geração do evento S-2206, siga os procedimentos abaixo conforme a situação identificada:

**Situação 1: Data de alteração anterior à data de virada do eSocial**

**(1)** Acesse a tela **"Empresas"** (Pessoal+ » Cadastros » Empresas) e verifique a **data de virada do eSocial** cadastrada para a empresa.

![Imagem 1: (1) Acesse a tela "Empresas" (Pessoal+ » Cadastros » Empresas) e verifique a data de virada do eSocial cadastrada para…](https://ajuda.sankhya.com.br/hc/article_attachments/41146484057239)

**(2)** Certifique-se de que a **data da alteração salarial** seja **posterior à data de virada** do eSocial. Caso contrário, o sistema não gerará o evento.

**(3)** Realize novamente o ajuste salarial com data posterior à virada do eSocial, se necessário.

**(4)** Acesse a **"Central de Eventos do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e execute a **geração completa** dos eventos.

**Situação 2: Situação do e-social incorreto**

**(1)** Acesse a tela **"Configuração Funcionários"** (Configurações » Cadastros » Pessoal » Configuração Funcionários).

**(2)** Localize o campo **"Situação no eSocial"** e verifique sua configuração.

![Imagem 2: (2) Localize o campo "Situação no eSocial" e verifique sua configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/41146973229719)

Se o campo estiver definido como **"Oficial: S-2200 e S-2300"**, a geração do evento **S-2206** não será realizada. Nessa situação, é necessário que o campo seja atualizado para **"Oficial: S-2205, S-2206 e S-2306"**.

Para efetuar essa atualização, basta realizar o **fechamento da folha na referência de admissão do funcionário**. Por exemplo, para colaboradores admitidos na referência **04/2026**, o campo será atualizado automaticamente após o fechamento da folha da competência **04/2026** na tela **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas). 

**(3)** Acesse a **"Central de Eventos do eSocial"** (Pessoal+ » Rotinas Folha » Central do eSocial) e execute a **geração completa** de todos os eventos.

**CAUSA**

A não geração do evento S-2206 pode ocorrer por diferentes motivos:

- **Data de alteração anterior à virada do eSocial:** O sistema não gera eventos com data anterior à data de virada cadastrada na empresa.
- **Situação no eSocial:** Incorreto
