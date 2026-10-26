---
id: "360044657914"
titulo: "Vinculação de NF-e de Compra de Emissão Própria na emissão do MDF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044657914-Vincula%C3%A7%C3%A3o-de-NF-e-de-Compra-de-Emiss%C3%A3o-Pr%C3%B3pria-na-emiss%C3%A3o-do-MDF-e"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Documentos Fiscais Eletrônicos > MDF-e"
atualizado_em: "2026-09-15T16:56:54Z"
rotulos: ["MDF-e", "Configuração", "NF-e", "XML", "Transporte", "Parceiro Remetente", "UFCOLCOMPMDFE", "UFCOLDESCMANUAL", "Sem Parceiro usa UF de Coleta do MDF-e", "Inclua NF-e de Compra no MDF-e com dados do Parceiro Remetente", "Parâmetro permite definir manualmente UFs e Municípios", "Documentos Eletrônicos"]
---

# Vinculação de NF-e de Compra de Emissão Própria na emissão do MDF-e

Através de nosso sistema, será possível realizar a inclusão de NF-e de Compra de Emissão Própria na emissão do MDF-e. Desta forma, as tag's de UF de Início e Município de Carregamento utilizarão os dados do **"Parceiro Remetente"**, informado na Central de Compras (grade **"Rodapé"**, aba **"Transporte"**) e a UF Fim e o Município de Descarregamento utilizarão os dados da Empresa da NF-e vinculada ao MDF-e.

**Observação:** para que o MDF-e seja emitido nas condições acima, é necessário que a NF-e vinculada ao MDF-e tenha o Tipo de Movimento igual à Compra que o Parceiro Remetente tenha sido informado. Quando o campo Parceiro Remetente não for informado e o parâmetro **"Considerar UF Coleta XML MDF-e Envolve Mov Compra? - UFCOLCOMPMDFE"** estiver ligado, o sistema considerará como UF inicial no XML a UF de Coleta da Aba Geral do MDF-e.

Considere ainda que, ao habilitar o parâmetro **"UF Coleta e UF Descarregamento manualmente - UFCOLDESCMANUAL"** será possível indicar manualmente a **"UF de Coleta"** e o **"Município de Coleta"**, bem como, a **"UF de Descarregamento"** e o **"Município de Descarregamento"** diretamente na sub-aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#sub-abageral), aba [MDF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abamdf-e) da tela [Viagens de Transporte (MDF-e)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514).

Este parâmetro será priorizado sempre que no MDF-e houver apenas documentos de emissão própria, ou seja, se a marcação **"Contém documentos de terceiros?"** estiver desativada na aba [Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612514-Viagens-de-Transportes-MDF-e#abageral) da tela Viagens de Transporte (MDF-e). Do contrário, a funcionalidade do parâmetro UFCOLCOMPMDFE será executada prioritariamente.
