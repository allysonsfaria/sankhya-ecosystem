---
id: "39543916490775"
titulo: "Novo PIX Integrado (Banco do Brasil) no PDV e Sankhya Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39543916490775-Novo-PIX-Integrado-Banco-do-Brasil-no-PDV-e-Sankhya-Checkout"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T13:28:20Z"
rotulos: ["Configuração", "PDV", "Financeiro", "Sankhya Checkout", "PIX", "Banco do Brasil"]
---

# Novo PIX Integrado (Banco do Brasil) no PDV e Sankhya Checkout

## 1. Pré-requisito:

Para utilizar esta funcionalidade, é necessário atender aos seguintes requisitos de versão:

- O administrador da empresa deve assegurar que as etapas de [**Contratação** e **Credenciamento (Fintech)**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36268652893591-PIX-imediato#4-jornada-de-uso) estejam devidamente concluídas.
- **PDV Web:** versão **4.35b463** ou superior
- **Sankhya Checkout:** versão **4.35b2604011844** ou superior e **SankhyaOM** versão **4.35b610** ou superior.
- Atualmente, o PIX Imediato nas **rotinas Varejo** é compatível com Banco do Brasil e futuramente Banco Itaú.

### 2. Configuração Sankhya Checkout

Após concluir as etapas de **Contratação** e **Credenciamento (Fintech)**, é fundamental realizar os procedimentos abaixo para que o Sankhya Checkout econheça as novas definições.

**2.1. Cadastro de Contas**

- Acesse: **Configurações » Cadastros » Bancários » Contas**
- Na aba **Castrados**, informe o **código da Empresa**.
- Na aba **PIX**, limpe os seguintes campos:
  - Chave da API PIX
  - Client Secret Pix
  - Client ID Pix
  - Chave Pix
- Mantenha o campo **“Utiliza PIX PDV”** marcado.

**2.2. Cadastro da Empresa**

- Acesse: **Comercial » Preferências » Empresa**
- Na aba **PIX**:
  - Altere o campo **“Tipo de PIX”** para **PIX Fintech**
- **Observação:**
  Após salvar a alteração, o campo **“Conta Fintech”** deverá ser preenchido com conta configurada no passo anterior. Caso isso não ocorra, revise as etapas anteriores de configuração.

**2.3. Finalização da Configuração**

Após concluir o cadastro, é fundamental realizar os procedimentos abaixo para que o Checkout Web reconheça as novas definições e não gere conflitos com parametrizações antigas:

1. **Limpeza do PIX Antigo (Contas):** acesse a tela de [**Contas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115113-Contas) e apague as configurações do PIX antigo/estático vinculadas àquela conta. Se você mantiver os dados antigos preenchidos, o Checkout tentará ler a configuração obsoleta, o que fará o novo PIX falhar.
2. **Sincronização Forçada:** no Sankhya Checkout (Menu >> Central de Sincronização >> Gerenciar Sincronizações), force a sincronização dos dados de **Empresa** e **Fintech**. Por que isso é necessário? A sincronização da Empresa vincula a conta bancária ao PDV, e a da Fintech busca os dados específicos de integração para a geração do QR Code.
3. **Limpeza de Cache:** o Checkout armazena diversos arquivos temporários para performance. Para garantir a leitura da nova configuração do PIX, feche o navegador ou a aplicação do Checkout por completo e abra novamente para iniciar uma sessão limpa.

## 3. Configuração PDV WEB

Após concluir as etapas de **Contratação** e **Credenciamento (Fintech)**, é fundamental realizar os procedimentos abaixo para que o **PDV Web** reconheça as novas definições:

**3.1. Cadastro de Contas**

- Acesse: **Configurações » Cadastros » Bancários » Contas**
- Na aba **Castrados**, informe o **código da Empresa**.
- Na aba **PIX**, limpe os seguintes campos:
  - Chave da API PIX
  - Client Secret Pix
  - Client ID Pix
  - Chave Pix
- Mantenha o campo **“Utiliza PIX PDV”** marcado.

**3.2. Cadastro da Empresa**

- Acesse: **Comercial » Preferências » Empresa**
- Na aba **PIX**:
  - Altere o campo **“Tipo de PIX”** para **PIX Fintech**
- **Observação:**
  Após salvar a alteração, o campo **“Conta Fintech”** deverá ser preenchido com conta configurada no passo anterior. Caso isso não ocorra, revise as etapas anteriores de configuração.

**3.3. Validação**

- Acesse: **Portal de Caixa » PDV Web**
- Realize uma venda utilizando o recebimento via **PIX**

## 4. Pontos de Atenção para o Suporte/Implantação

| **Situação** | **Causa Provável** | **Solução** |
| --- | --- | --- |
| **Mensagem: "Serviço não contratado"** | Falta concluir a etapa 4.1 do guia Fintech. | Ativar o pacote no Assistente de Melhores Práticas. |
| **QR Code não é gerado** | Credenciais (ID/Secret) incorretas ou conta não credenciada. | Revisar a Etapa 4 do credenciamento da conta. |
| **Venda não finaliza após o pagamento** | Baixa automática não configurada. | Ajustar as "Ações Automáticas" no credenciamento da conta (Etapa 3). |
| Configurações alteradas não refletem no Checkout | Excesso de cache ou falta de sincronia. | Forçar sincronização (Empresa/Fintech) e reiniciar o navegador/aplicativo. |
| Novo PIX não funciona / QR Code não é gerado. | Configurações obsoletas na conta ou credenciais incorretas. | Acessar a tela de Contas e limpar o cadastro do PIX antigo. |

## 5. Links de Apoio

- [Central de Ajuda: PIX Imediato](https://ajuda.sankhya.com.br/hc/pt-br/articles/36268652893591-PIX-imediato)
- [Central de Ajuda: Boleto Rápido](https://ajuda.sankhya.com.br/hc/pt-br/articles/5840766689559-Boleto-r%C3%A1pido-API)
- [Detalhes de Cobrança](https://ajuda.sankhya.com.br/hc/pt-br/articles/14550240434839-Detalhes-de-cobran%C3%A7a-de-servi%C3%A7o-do-Boleto-r%C3%A1pido)
