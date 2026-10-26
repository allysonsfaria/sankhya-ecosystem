---
id: "19672626516119"
titulo: "Como lançar atrasos para desconto do DSR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR"
trilha: "Manual do Produto > Pessoas+ > Afastamentos e Ocorrências > Faltas e Atrasos"
atualizado_em: "2026-10-02T15:32:29Z"
rotulos: ["Configuração", "Folha de Pagamento", "Regras de cálculo", "br.com.sankhya.rh.LancAtrasosDescDSR", "Lançamento de Atrasos para Desconto de DSR", "Pessoal+", "DSR", "Ponto Eletrônico", "Atrasos"]
---

# Como lançar atrasos para desconto do DSR

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:** br.com.sankhya.rh.LancAtrasosDescDSR

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SS2JZRYDG9NSXT5P3HV09Q)

- [1. Descrição da Funcionalidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SRFF8S47CAW53YY5XXFHFB)
- [2. Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SRMAAFXDQ2VQHZEKBVPW3A)
- [3. Diagrama de Fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SRXP4CT124PVKZ9WHR4J8C)
- [4. Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SRZR01GN4J4PC471QTEKSY)
- [5. Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SSGXW88GB6R03WHBZQCA07)
- [6. Dicas de Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SSK83BEG09WJ6QBBY2JHHE)
- [7. Casos de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SSMTACDKNQHBACB13AQFDT)

[FAQ – Dúvidas Frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K80X7DGE3XDB7Y4C541K9495)

[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/19672626516119-Como-lan%C3%A7ar-atrasos-para-desconto-do-DSR#h_01K7SSQH6XNZ5KT8C58S9PD8S4)

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

Permite registrar atrasos para desconto de DSR (Descanso Semanal Remunerado) na folha de pagamento do funcionário. Garante que os atrasos sejam considerados conforme regras da empresa, automatizando o cálculo do desconto quando aplicável.

### 2. Pré-requisitos

**Permissões necessárias**

- Acesso ao módulo Pessoal+ e Rotinas Folha.

**Parâmetros essenciais**

- Na Regra de Cálculo da empresa, aba [Ponto](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007-Regras-de-C%C3%A1lculo#abaponto), o campo **Atualiza Atrasos p/ Descontos de DSR** deve estar configurado como **Sempre Atualiza** e o campo **Limite de Atrasos para Perda de DSR** definido com um valor inferior ao atraso lançado.

**Configurações relacionadas**

- Integração do ponto eletrônico com folha de pagamento (opcional).

### 3. Diagrama de fluxo

![Imagem 1: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/35710037769623)

### 4. Jornada de Uso

1. Acesse a tela **Lançamento de Atrasos para Desconto de DSR** (Pessoal+ > Rotinas Folha.![Imagem 2: Acesse a tela Lançamento de Atrasos para Desconto de DSR (Pessoal+ > Rotinas Folha.](https://ajuda.sankhya.com.br/hc/article_attachments/19672923992215)
2. Clique em ![Imagem 3: Clique em Cadastrar Lançamento de Atrasos para Desconto de DSR para iniciar um lançamento.](https://ajuda.sankhya.com.br/hc/article_attachments/19672923997591) **Cadastrar Lançamento de Atrasos para Desconto de DSR** para iniciar um lançamento.
3. Selecione a **Empresa** e o **Funcionário**.
4. Informe a **Data do Atraso**.
5. Na aba **Geral**:
   - o campo **Origem** é preenchido automaticamente conforme integração do ponto com a folha de pagamento;
   - informe a quantidade de minutos ou horas do atraso e marque a opção **Perde DSR**.
6. Clique em ![Imagem 4: Clique em Salvar (F7) e o desconto será calculado automaticamente na folha, se as regras forem atendidas.](https://ajuda.sankhya.com.br/hc/article_attachments/19672979102487) **Salvar [F7]** e o desconto será calculado automaticamente na folha, se as regras forem atendidas.

### 5. Pontos de Atenção

- O desconto de DSR só ocorre se o atraso lançado for superior ao **Limite de Atraso para Perda de DSR** definido nas regras de cálculo.
- Para lançamentos manuais, o campo **Origem** deve estar como **Manual** e a opção **Perde DSR** marcada.
- Configurações incorretas podem impedir o cálculo do desconto.

### 6. Dicas de Usabilidade

- Utilize o atalho F7 para salvar o cadastro rapidamente.
- O preenchimento do campo **Origem** é automático quando há integração de ponto eletrônico.
- Revise os campos das regras de cálculo antes de realizar lançamentos.

### 7. Casos de Uso

**✅ Exemplo Real**

Colaborador com atraso superior ao limite configurado, lançamento manual com **Perde DSR** marcado, desconto aplicado na folha.

**❌ Erro Comum**

Lançamento realizado sem configurar o campo **Atualiza Atrasos p/ Descontos de DSR** como **Sempre Atualiza**, impedindo o desconto.

## FAQ - Dúvidas Frequentes

**1. Quando o desconto de DSR é aplicado automaticamente?**

Quando o atraso lançado excede o limite definido nas regras de cálculo.

**2. Posso lançar atrasos para qualquer funcionário?**

Sim, desde que tenha permissão e os parâmetros estejam configurados corretamente nas regras de cálculo.

**3. O campo "Origem" pode ser alterado manualmente?**

Não, ele é preenchido conforme a integração do ponto eletrônico.

## Artigos Relacionados

- [Regras de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405310442007)
