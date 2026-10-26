---
id: "37884665805079"
titulo: "Como cadastrar Máscaras e Locais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37884665805079-Como-cadastrar-M%C3%A1scaras-e-Locais"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-07-22T14:05:57Z"
rotulos: ["Configuração", "WMS", "Estoque", "Cadastro", "Squad WMS"]
---

# Como cadastrar Máscaras e Locais

## O que é o cadastro da máscara de locais e dos locais?

A máscara define a estrutura hierárquica dos locais de estoque no sistema. Essa configuração é essencial, pois determina como os níveis (como armazém, rua, prateleira, posição, etc.) serão organizados. Por isso, deve ser realizada antes do cadastro dos locais, já que, após ser utilizada, não poderá mais ser alterada.

O cadastro de locais permite uma gestão mais eficiente dos produtos e materiais dentro da empresa. Essa organização contribui para o controle do estoque, melhora a rastreabilidade e otimiza as operações logísticas e de produção.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/864578922)

#### Cadastre a máscara que será utilizada no cadastro dos locais

1. Cadastro de **Máscara para local**

- Acesse a tela **Máscara para Local**

**Menu:** Configurações » Avançado » Máscara para Local

- Defina a estrutura da máscara:
- A máscara pode conter até 4 níveis hierárquicos
- Informe a quantidade de dígitos para cada nível
- Exemplo de estrutura: "**99\999\99**", neste exemplo, a configuração seria:
- Nível 1 - 2
- Nível 2 - 3
- Nível 3 - 2
- Nível 4 - 0
- Clique em **Salvar**

#### Observações importantes

- O primeiro nível da máscara representa os **locais principais**, como um armazém, por exemplo.
- Os níveis seguintes são usados para **divisões internas**, como corredores, prateleiras ou posições.
- Planeje bem a estrutura da máscara antes de salvar, pensando também em possíveis **ampliações no futuro**.
- A máscara pode ter **até 4 níveis** e no máximo **9 dígitos somando tudo**.
- Os níveis podem ter **quantidades diferentes de dígitos** (ex: 2 no primeiro nível, 3 no segundo, etc.).
- Depois que você cadastrar o primeiro local, **não será mais possível mudar a máscara**.
- Essa estrutura será usada em **todos os locais de estoque** da empresa, então é importante que atenda às necessidades do negócio.

#### Cadastre os locais que serão utilizados

1. Cadastro de **Locais**

- Acesse a tela **Locais**

**Menu:** Comercial » Arquivo » Cadastros » Locais

- Clique em **+ Novo Registro** e preencha os campos:
- **Código**: Informe o código do local conforme a estrutura definida na máscara. Considerando o exemplo anterior de máscara, poderiamos usar: “**01.001.00**”
- **Descrição**: Preencha com o nome do local (ex: Depósito Central, Prateleira A1).
- Marque a opção "**Ativo**" para que o local possa ser usado.
- Marque "**Analítico**" se o local não terá sublocais (chamados de “filhos”) ou caso ele seja um sublocal.
- Se for um sublocal, o código deve ser corresponde ao cadastro “pai”  para vinculo com este local principal, considerando nosso exemplo, teríamos: “**100000**” local “pai” ou sintético (flag “Analítico” desmarcada)  e “**01.001.00**” local “filho” e analítico.

#### Observações importantes

- O local precisa estar **ativo** para ser utilizado nas rotinas do sistema.
- A opção **"Analítico"** indica que o local **não pode ter subníveis**.
- É possível montar uma **estrutura hierárquica** com locais e sublocais.
