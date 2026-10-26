---
id: "360048820694"
titulo: "É possível utilizar o mesmo certificado digital para matriz e filiais?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048820694-%C3%89-poss%C3%ADvel-utilizar-o-mesmo-certificado-digital-para-matriz-e-filiais"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:31:20Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "#validacaoWellington", "Uso do Certificado Digital em Matriz e Filiais", "Certificado Digital", "Documentos Eletrônicos"]
---

# É possível utilizar o mesmo certificado digital para matriz e filiais?

**![Imagem 1: O certificado digital de um estabelecimento situado em uma UF é válido para outras UFs ou é preciso que cada…](https://ajuda.sankhya.com.br/hc/article_attachments/18789314269335) O certificado digital de um estabelecimento situado em uma UF é válido para outras UFs ou é preciso que cada estabelecimento tenha um certificado digital próprio?**

- O certificado digital é válido para toda a empresa, possua ela um ou mais estabelecimentos. Assim, o certificado digital do estabelecimento de qualquer UF, seja ele matriz ou filial, pode ser utilizado para os demais estabelecimentos da empresa localizados em unidades federadas.

**![Imagem 2: Caso minha empresa possua vários estabelecimentos que irão emitir NF-e, será necessário adquirir um certificado digital…](https://ajuda.sankhya.com.br/hc/article_attachments/18789306124055) Caso minha empresa possua vários estabelecimentos que irão emitir NF-e, será necessário adquirir um certificado digital para cada estabelecimento?**

- Não, a empresa poderá optar por utilizar o certificado digital de qualquer um de seus estabelecimentos para emitir as NF-e de todos os estabelecimentos.

**![Imagem 3: O certificado digital pode ser instalado em mais de um computador ou apenas no utilizado pelo programa emissor das…](https://ajuda.sankhya.com.br/hc/article_attachments/18789306126487) O certificado digital pode ser instalado em mais de um computador ou apenas no utilizado pelo programa emissor das notas?**

- A instalação do certificado digital deverá **obedecer ao disposto na respectiva política de certificado da Autoridade Certificadora que o forneceu**. Existem certificados que podem ser instalados em mais de um computador, e certificados que não possibilitam esta prática.

Fonte: [Perguntas Frequentes - SEFAZ](https://www.nfe.fazenda.gov.br/portal/perguntasFrequentes.aspx?tipoConteudo=k/E5BakB80o=#:~:text=Sim%2C%20o%20certificado%20digital%20utilizado,utilizado%20tamb%C3%A9m%20no%20SPED%20Fiscal.&text=Assim%2C%20o%20certificado%20digital%20do,empresa%20localizados%20em%20unidades%20federadas.)

**![Imagem 4: Como funciona a instalação do mesmo certificado para Matriz e Filial dentro do sistema ?](https://ajuda.sankhya.com.br/hc/article_attachments/18789314288023) Como funciona a instalação do mesmo certificado para Matriz e Filial dentro do sistema ?**

No sistema, é necessário cadastrar somente 1(UM) certificado na tela 'Console NF-e': o certificado da Matriz.

O sistema reconhece as filiais pelo Radical do CNPJ, assim ele sabe que pode utilizar aquele certificado para todas as empresas com mesmo radical do CNPJ.

**![Imagem 5: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/18789314292119) IMPORTANTE:**

- As empresas podem realizar mudanças de Matriz/CNPJ, considere o exemplo:
- Matriz com CNPJ 00.000.0001/00, deixa de ser Matriz.
  O CNPJ 00.000.0055/00 passa a ser Matriz.
- Por padrão o sistema considera o CNPJ 00.000.0001/00 com o 0001 como matriz.

Porém, na inserção do certificado, é possível indicar outro cnpj como matriz, através da marcação abaixo:

- Campo **"Matriz"**, tela 'Console NF-e', aba 'Registro de Certificado'.

 Para mais detalhes: [O que é Certificado digital e para que serve?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044295653)
