---
id: "37885172957463"
titulo: "Como cadastrar Serviços"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37885172957463-Como-cadastrar-Servi%C3%A7os"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-07-29T14:45:50Z"
rotulos: ["ISS", "Configuração", "Serviços", "Impostos", "NFS-e", "Cadastro"]
---

# Como cadastrar Serviços

## Por que o cadastro de serviços é importante e o que deve ser considerado ao realizá-lo?

O cadastro de serviços é essencial para a gestão e operação das empresas, garantindo organização, precificação correta e compliance fiscal. Um registro bem-feito evita erros e assegura o bom funcionamento do sistema.

Um cadastro de serviços bem estruturado facilita a gestão operacional, assegura a correta precificação e tributação, além de garantir a geração precisa de relatórios fiscais e gerenciais.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/864947338)

#### Cadastre os seus serviços conforme passo a passo abaixo. As informações devem ser peenchidos conforme os dados fornecidos

1. Cadastro de serviços

- Acesse a tela **Serviços**

**Menu:** Configurações » Cadastros » Produtos » Serviço

- Clique em **+ Novo registro** e preencha os campos:

**Painel Principal**

- **Descrição:** Preenchimento obrigatório. Informe a descrição do serviço.
- **Ativo:** Marque para que o serviço esteja disponível para uso.

**Aba Geral**

- **Grupo:** Selecione o grupo ao qual o serviço pertence (precisa estar previamente cadastrado).
- **Unidade Padrão:** Escolha a unidade de medida (ex: Horas, Minutos, Dias – deve estar cadastrada na tela de Unidades).

**Aba Impostos**

- Marque **"Tem ISS"** como **Tributado.**
- **Código de Tributação Município NFS-e**
- **CNAE da empresa**
- **Tipo de Serviço (conforme lista LCP 116)**
- Marque **"Tem INSS",** se houver incidência
- **%Red. Base INSS (se houver)**
- **Imposto de Renda (IRF)**
- Marque **"Tem IRF",** se o serviço estiver sujeito ao imposto.
- **% IRF** (ex: 1,5%)
- **Grupo PIS, Grupo COFINS e Grupo CSLL:** Vincule os grupos previamente cadastrados.
- **Tipo de Serviço:** Vincule corretamente para fins de tributação.
- Clique em **Salvar**.

**Aba Alíquotas de ISS**

- Clique em **+ Novo registro** e preencha:
- **Cidade:** Informe onde a alíquota será aplicada.
- **Empresa:** Selecione a empresa vinculada.
- **Percentual de ISS:** Informe a alíquota.
- **Código de Tributação ISS:**

00 – Tributado

01 – Tributado com ISS Retid

06 – Isento

07 – Não Tributado

- **Tipo de Serviço:** Vincule o código correspondente.
- **Percentual de dedução na base do ISS:** Preencha se houver dedução.
- **Tipo de Dedução da Base de ISS**

Subempreito

Por percentual

Matérias

(Em branco, se não houver)

- Clique em **Salvar**

**Aba Outros Impostos**

- Clique em **+ Novo registro** e preencha:
- **Imposto**
- **Alíquota**
- **Na Nota:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto na nota
- **No Financeiro Origem Financeiro:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto no financeiro quando de origem financeiro
- **No Financeiro Origem Estoque:** Informe qual deve ser o comportamento sistema quanto a retenção desse imposto no financeiro quando de origem estoque
- **Ponto de atenção**: Para que os impostos sejam viculados aqui eles devem ser cadastrados de forma prévia na tela **Impostos**.
- Clique em **Salvar**

#### Observações importantes

- As configurações devem seguir a **legislação vigente** e as **regras do município** onde o serviço será prestado.
- Os **grupos de PIS, COFINS e CSLL** devem estar cadastrados antes.
- Para **NFS-e**, o **código de tributação do município** deve ser corretamente preenchido.
- A alíquota de ISS pode ser cadastrada diretamente na tela de serviço.
- Para serviços **isentos ou não tributados**, use a tela específica de **Alíquotas de ISS**.
