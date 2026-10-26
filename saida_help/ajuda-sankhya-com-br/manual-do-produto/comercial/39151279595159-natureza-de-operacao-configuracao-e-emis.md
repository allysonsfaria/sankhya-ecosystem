---
id: "39151279595159"
titulo: "Natureza de Operação - Configuração e Emissão"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39151279595159-Natureza-de-Opera%C3%A7%C3%A3o-Configura%C3%A7%C3%A3o-e-Emiss%C3%A3o"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-08-07T13:14:39Z"
rotulos: ["Configuração", "Fiscal", "Impostos", "Natureza", "Prefeituras", "NFS-e", "Natureza de Operação", "Json", "Natureza de Operação - Configuração e Emissão", "br.com.sankhya.mgecom.NaturezaOperacao"]
---

# Natureza de Operação - Configuração e Emissão

**Módulo:** Comercial

**Caminho:** Comercial > Arquivo > Cadastros > Natureza de Operação.

---

Este guia mapeia o passo a passo completo do Analista Fiscal para garantir que a emissão da NFS-e atenda às exigências de códigos específicos de cada município (como a exigência de 3 dígitos ou formatos alfanuméricos), utilizando a nova estrutura desvinculada do [Tipo de Operação (TOP)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP).

#### Fase 1: o cadastro base (preparação)

A jornada começa com a criação do catálogo de naturezas de operação que a sua empresa precisará utilizar perante as prefeituras.

[GIF animado: Imagem 1: A jornada começa com a criação do catálogo de naturezas de operação que a sua empresa precisará utilizar perante as…](https://ajuda.sankhya.com.br/hc/article_attachments/39154089119511)

- **Onde ir:** acesse **Comercial > Arquivo > Cadastros > Natureza de Operação**.
- **Ação do Usuário:** você visualiza os registros padrões do sistema e pode clicar em **Novo (+)** para cadastrar os códigos específicos exigidos pelo município onde presta serviço.
- **O que preencher:** além do **Código** e da **Descrição**, você deve configurar o campo **Imune/Isenta**. Marque esta opção como **Sim** sempre que a natureza da operação não for tributada. Para facilitar seu trabalho, o sistema já pré-configura automaticamente como "Sim" as naturezas nacionais conhecidas (como os códigos 05, 09, 3, 4, M, N, R, entre outros), mas você pode alterar essa marcação conforme a orientação fiscal da sua prefeitura.

#### Fase 2: a parametrização estratégica (vinculação)

Com o catálogo criado, o analista precisa dizer ao sistema quando usar cada código. O sistema Sankhya é inteligente e permite aplicar a regra em três níveis diferentes. O usuário escolhe o nível adequado de acordo com o cenário da empresa:

- **Cenário A (Faturamento Recorrente):** se a empresa fatura por contratos e aquele contrato possui uma natureza específica, o usuário acessa a tela de [**Contratos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos), vai até a aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044604774-Contratos#abaimpostos) e seleciona o **Cód. Natureza de Oper. ISS (NFS-e)**.

![Imagem 2: Cenário A (Faturamento Recorrente): se a empresa fatura por contratos e aquele contrato possui uma natureza específica,…](https://ajuda.sankhya.com.br/hc/article_attachments/39151279588247)

- **Cenário B (Regra Tributária):** se a empresa realiza faturamentos avulsos baseados em regras de ISS, o usuário acessa a tela de [**Alíquotas de ISS**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS), na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601014-Al%C3%ADquotas-de-ISS#abageral), e vincula a natureza correspondente, também pelo campo **Cód. Natureza de Oper. ISS (NFS-e)**.

![Imagem 3: Cenário B (Regra Tributária): se a empresa realiza faturamentos avulsos baseados em regras de ISS, o usuário acessa a…](https://ajuda.sankhya.com.br/hc/article_attachments/39151279589527)

- **Cenário C (Regra Padrão do Serviço):** Se a natureza for sempre a mesma para um determinado serviço prestado por aquela empresa, o usuário acessa o cadastro de [**Serviço**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o), na aba [Configurações por Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110553-Cadastro-de-Servi%C3%A7o#abaconfiguraesporempresa), e faz o vínculo, por meio do campo **Cód. Natureza de Oper. ISS (NFS-e)**.

![Imagem 4: Cenário C (Regra Padrão do Serviço): Se a natureza for sempre a mesma para um determinado serviço prestado por aquela…](https://ajuda.sankhya.com.br/hc/article_attachments/39151303965591)

#### Fase 3: validação de pré-requisito (atenção do analista)

Para que todo o trabalho da Fase 2 tenha efeito prático na comunicação com a prefeitura, há uma chave que precisa estar ligada.

- **Ação do Usuário:** o analista acessa o cadastro de [**Cidades**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110913-Cidades), localiza o município de prestação do serviço e garante que a marcação **"Gerar Código Natureza Operação ISS no Json"** esteja habilitada. Sem isso, o sistema não enviará a informação no json para emissão.

#### Fase 4: a emissão da NFS-e (automação do sistema)

Nesta fase, o faturista entra em ação. Ele não precisa se preocupar em preencher a natureza de operação manualmente na nota. O sistema fará o trabalho pesado sozinho.

- **O que acontece nos bastidores:** ao confirmar a NFS-e (seja avulsa ou gerada via contrato), o sistema avaliará a nota e aplicará o código correto respeitando uma rigorosa **Hierarquia de Prioridades**:
  1. O sistema olha primeiro para o **Contrato**. Tem natureza configurada lá? Se sim, ele usa essa e ignora o resto.
  2. Se não tiver contrato, ele olha para a **Alíquota de ISS**. Tem natureza vinculada (>0)? Se sim, ele usa essa.
  3. Se não tiver na alíquota, ele olha para o **Serviço** (aba Configurações por Empresa).
  4. Se estiver tudo vazio, ele usa a configuração da **TOP**.

**Inteligência de Imunidade (ISS):** se você utilizar uma natureza configurada como **Imune/Isenta** (na Fase 1), o sistema ativa automaticamente uma regra adicional de conformidade para o Padrão Nacional. Ele busca o **Tipo de Imunidade ISS** no cadastro do **Parceiro** (Aba Fiscal) para preencher a tag específica no JSON.

| **Dica**  Se você emitir uma nota imune ou isenta, mas o cadastro do parceiro estiver com o tipo de imunidade vazio, o sistema assume automaticamente o código **"1 - Patrimônio, renda ou serviços, uns dos outros"**. Essa automação evita que a prefeitura rejeite a sua nota por omissão de informação. |
| --- |

- **Resultado final:** o JSON recebe o código exato da natureza e, se aplicável, o tipo de imunidade correspondente. Assim, a nota é autorizada sem rejeições e sem a necessidade de intervenção manual no momento da emissão.
