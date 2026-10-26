---
id: "360044606534"
titulo: "Associar Cheque ao CMC7"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044606534-Associar-Cheque-ao-CMC7"
trilha: "Manual do Produto > Financeiro e Patrimônio > Financeiro"
atualizado_em: "2026-07-29T14:39:55Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "CMC7", "Movimentação Financeira", "Financeiro", "Cheque", "Associar Cheque ao CMC7", "br.com.sankhya.associar.cheque.cmc7", "Associar Cheque ao CMC7 manual", "Identificação do CMC7", "Associação de cheques", "Utilização de leitor"]
---

# Associar Cheque ao CMC7

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312348907159) Módulo: Financeiro> Rotinas
```

---

O CMC7 é um padrão de identificação automática de cheques criado e amplamente utilizado na Europa e também adotado por outros países, incluindo o Brasil. CMC7 é sigla de Caracteres Magnéticos Codificados em Sete Barras. Além do CMC7, existem outros padrões de identificação automática de cheques, como o E13B (utilizado nos Estados Unidos) e o OCR. O CMC7 cheque representa números de 0 a 9 e letras de A a Z, além de alguns caracteres especiais como **">"** (maior), **"<"** (menor) e ":" (dois pontos).

O [Banco Central do Brasil](http://www.bcb.gov.br/pt-br#!/home) é a entidade responsável por estabelecer o layout do cheque. A chamada banda magnética do CMC7 contêm as seguintes informações:

- Número da câmara de compensação;
- Número do banco;
- Número da agência;
- Número da conta corrente;
- Número do cheque.

Através desta tela, informe os  dados do cheque manualmente ou através de um leitor. A consulta feita através do CMC7, quer seja através de digitação, quer através de micro terminais com leitura óptica, possibilita o recebimento de cheques com maior segurança, evitando a recepção de cheques clonados, adulterados, fraudados etc.

![Imagem 2: Através desta tela, informe os dados do cheque manualmente ou através de um leitor. A consulta feita através do CMC7,…](https://ajuda.sankhya.com.br/hc/article_attachments/8497330572823)

Nos campos Comp, Banco, Agência, Conta e Cheque só é permitida a digitação de números.

O campo **"Prefixo do cheque"** é preenchido automaticamente de acordo com o Banco inicialmente informado.

**Tipos de Cheques:** Neste campo, pode-se trabalhar com os seguintes tipos de cheque:

- **Normal:** Cheque utilizado normalmente por titulares de conta corrente em instituições bancárias;
- **Bancário:** Cheque avulso emitido por instituição bancária na impossibilidade do correntista fazê-lo (pelos mais diversos motivos);
- **Salário:** Cheque que a empresa emite exclusivamente para pagamento de salários aos seus funcionários;
- **Administrativo:** Cheque que qualquer pessoa compra em um banco. O solicitante paga o serviço da emissão do cheque e os fundos necessários para sua liquidação. O banco emite o cheque nominalmente a algum beneficiário e garante os fundos;
- **CPMF:** Também conhecido como TB (Transferência Bancária). É emitido pelo titular da conta que é utilizada apenas para transferência de fundos entre contas de mesma titularidade sem incidência do CPMF.

Para utilização de um leitor, você deverá posicionar o cursor do mouse abaixo do botão **"Gerar Banda"**. Ao passar o cheque na leitora, a Banda será preenchida.

Ao clicar em Gerar Banda manualmente, serão utilizados dados básicos como **"banco"**, **"agência"**, **"conta"** e **"número do cheque"** para preencher as três seções dos campos.

Pode-se também digitar os números da banda da tarja do cheque no campo **"Banda CMC7"**, caso a leitora não consiga ler a tarja do cheque. A tarja possui 34 (trinta e quatro) caracteres. Vejamos um exemplo:

O formato da tarja é: <40909387<0013008805<400010347938:

Deve-se digitar apenas os números; os caracteres **"<"** e **":"** não devem ser incluídos.

Em seguida, clique no botão **"Validar Banda"**; nesse momento o sistema irá verificar se a banda é válida e preencherá os campos Comp, Banco, Agência, Conta e Cheque posicionados logo abaixo.

Ao clicar no botão **"Filtrar"**, o sistema irá identificar os títulos que possuem o número do cheque ou o CMC7 inicialmente informados, ou que possuam a banda do cheque salva no campo Código de Barras do título, e apresentá-los na grade inferior da tela. Sendo encontrado algum título que tenha o mesmo número de cheque e não contenha o código de barras preenchido, pode se associar o cheque cadastrado ao título selecionado por meio do botão **"Associar"**.

Previamente, pode-se proceder com a associação do cheque ao emitente, incluindo-se o número do cheque no campo **"Nosso número"** presente na aba **"Outras informações"** na tela [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874). Caso o cheque esteja associado a algum emitente, os campos **"Nome emitente"** e **"CPF/CNPJ do emitente"** serão preenchidos com a nomenclatura e CPF/CNPJ do emitente.

Caso os campos Nome emitente e CPF/CNPJ do emitente estejam vazios, sendo que você poderá informá-los manualmente; o sistema irá validar a numeração incluída no campo **"CPF/CNPJ do emitente"**.

Ao clicar no botão **"Associar"**, o título posicionado na grade que estiver com a coluna **"Código de Barras"** vazia, receberá a associação, ou seja, será preenchido com o número da banda.

Se o título já possuir o CMC7, não será possível realizar uma nova associação; será exibida a seguinte mensagem:

**"Associação não pode ser feita porque o título já possui CMC7."**

**Importante:** No caso de contas do [Banco do Brasil](http://www.bb.com.br/pbb/pagina-inicial#/), o dígito verificador **"X"** (campo C2), será substituído pelo **"0"** (zero); no caso das informações do cheque serem inseridas manualmente, o dígito **"X"** não deverá ser digitado no campo **"Conta"**.

O parâmetro **"Data sugerida na validação CMC7 - CMC7DTCHEQUE"**, possui duas opções, Data da baixa e Data do vencimento. Na utilização do CMC7, o campo Data do cheque será preenchido com a data definida neste parâmetro.
