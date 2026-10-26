---
id: "360044596474"
titulo: "Observações para Notas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-24T12:34:05Z"
rotulos: ["manual", "Configuração", "Fiscal", "NF-e", "SEFAZ", "Escrituração Fiscal Digital - EFD", "Impressão de notas fiscais", "Observações para Notas", "Padrões", "br.com.sankhya.com.cad.observacoesnotas", "Observações para Notas manual", "EFD", "Criação e Gestão de Observações para Notas Fiscais", "Observações"]
---

# Observações para Notas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310584801815) Módulo: Comercial > Arquivo > Cadastros
```

---

Através desta tela, é realizada a criação de observações padrões para serem impressas nas notas fiscais. Depois de cadastrada, basta informar seu correspondente código na digitação da nota.

![Imagem 2: Através desta tela, é realizada a criação de observações padrões para serem impressas nas notas fiscais. Depois de…](https://ajuda.sankhya.com.br/hc/article_attachments/10900852937623)

Ao cadastrar uma observação, deve-se proceder com o preenchimento dos seguintes dados:

Indique o **"Código"** para a observação a ser cadastrada; esta informação pode ser inserida de maneira automática ou manual, dependendo da definição feita no botão ![Imagem 3: Indique o "Código" para a observação a ser cadastrada; esta informação pode ser inserida de maneira automática ou…](https://ajuda.sankhya.com.br/hc/article_attachments/16672808902551) **"Configuração da Tela"** presente no alto da tela.

Preencha, em seguida, o aspecto principal da tela, ou seja, a **"Observação"** que será utilizada nos posteriores lançamentos de notas.

**Importante:** ao vincular uma Observação no [Cadastro de Alíquotas de ICMS](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602934-Al%C3%ADquotas-de-ICMS) e esta mesma observação no Item da Nota, campo **"Obs Padrão"**, após a escrituração e geração do [EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI), ao consultar o arquivo, o Registro C190 vinculado à esta Nota apresentará a Observação descrita no campo 12, bem como também será apresentada no Registro 0460.

**Nota:** caso seja apresentada apenas uma observação, o campo será preenchido com ela; por outro lado, apresentando-se mais de uma observação, o campo será ocupado com a primeira observação localizada.

Os campos mencionados abaixo são utilizados para geração de Escrituração Fiscal Digital - EFD, são eles:

Se a observação estiver ligada a algum processo, informe no campo **"Num. Processo"** o referido número (o número do processo impresso na Nota resguardará a empresa de quaisquer sanções de lei). Além disso, na geração dos registros do bloco E, bloco C, 1922 e 1926, este campo se comporta da seguinte maneira:

- Arquivos gerados até o exercício 2022, o campo permite até 15 caracteres;
- Arquivos gerados a partir do exercício 2023 poderão ter até 60 caracteres.

Determine no campo **"Origem Processo"** o órgão que deu origem ao processo correspondente ao campo anterior. Tem-se as seguintes opções:

- Secex/RFB;
- Justiça Federal;
- Sefaz;
- Justiça Estadual;
- Outros.

Ao efetuar a marcação **"Vincular DAE/GNRE"**, a empresa estará declarando que a observação gerada no Documento Fiscal dará ou deu origem a uma guia de recolhimento, DAE ou GNRE.

No campo **"Geração no EFD"** determine como será o comportamento da observação em questão, na geração da EFD. Pode-se defini-lo dentre as seguintes opções:

- **Não Gerar:** Por esta opção, as configurações desta tela não serão apresentadas no arquivo EFD;
- **Informações Complementares do Documento Fiscal:** Se selecionada esta opção, as configurações desta tela serão apresentadas no registro 0450 do EFD;
- **Observação do Lançamento Fiscal:** Através desta opção, as configurações desta tela serão apresentadas no registro 0460 do EFD.

A marcação **"Carrega Complemento p/ EFD"** quando realizada para um determinado código de observações, alimentará o campo 03 do registro C110 do EFD ([EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital-ICMS-IPI)), com a descrição cadastrada no campo Observação, tanto no cabeçalho da nota, quanto nos itens, conforme código configurado para a observação padrão.

Exemplos de observações:

- "Não aceitamos devolução de mercadorias”;
- "Obrigado pela preferência", etc.

O campo **Operação com ressarcimento/complemento de ST** permite indicar que uma **observação padrão** está relacionada a operações de ressarcimento ou complemento de ICMS-ST. Ao marcar essa opção, o sistema passa a considerar os movimentos fiscais associados a essa observação para inclusão nos registros **C180, C181, C185 e C186**, desde que a funcionalidade também esteja ativada na tela de [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa).

#### Seção Super Sintegra / SEF-II / EFD

Nesta seção, pode-se observar o campo **"Código de referência à informação complementar"**, os dados informados no mesmo serão utilizados quando a SEFAZ exigir um código específico para a observação. Além disto, na geração do Super Sintegra, SEF-II, EFD - Contribuições, EFD - Escrituração Fiscal Digital - ICMS/IPI e do SPED Fiscal tem-se a seguinte análise:

- Quando o campo Código de referência à informação complementar estiver preenchido, utiliza-se as informações do mesmo;
- Caso não contenha informações, emprega-se os dados contidos no campo **"Código"**.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474-Observa%C3%A7%C3%B5es-para-Notas#top)
