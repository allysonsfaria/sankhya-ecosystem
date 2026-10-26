---
id: "39352456965399"
titulo: "Como corrigir divergência de valores no Resumo da Folha com Desoneração"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352456965399-Como-corrigir-diverg%C3%AAncia-de-valores-no-Resumo-da-Folha-com-Desonera%C3%A7%C3%A3o"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:47Z"
rotulos: ["Configuração", "Desoneração", "Impostos", "Folha de Pagamento", "Gerenciador de Folhas", "13º Salário", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como corrigir divergência de valores no Resumo da Folha com Desoneração

Ao gerar o "Resumo da Folha" na rotina Gerenciador de Folhas (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), o sistema poderá apresentar valores divergentes quando a empresa possuir desoneração da folha de pagamento e houver cálculo de 13º salário na mesma competência.

É importante compreender como o sistema realiza a **composição dos valores** no resumo e como ajustar as informações quando necessário, garantindo que a **apuração dos valores** seja realizada corretamente.

### Como o sistema calcula o total do INSS

O comportamento do sistema para a apresentação do valor total de INSS no **"Resumo da Folha"**, disponível na rotina **Gerenciador de Folhas** (Pessoal+ » Rotinas Folha » Gerenciador de Folhas), ocorre da seguinte forma:

Para o cálculo da cota patronal (parte da empresa), o sistema considera as bases de INSS, com exceção da base de INSS referente ao 13º salário. Em seguida, é deduzido o valor correspondente ao salário-maternidade.

É importante destacar que essa dedução contempla apenas o valor do salário-maternidade referente à folha mensal, não sendo considerado o salário-maternidade incidente sobre o 13º salário. Isso ocorre porque, para empresas desoneradas, a base de INSS referente ao 13º salário não compõe a base de cálculo da contribuição patronal.

 **Exemplo prático de cálculo com 13º salário**

**Exemplo de cálculo da contribuição patronal na referência 12/26.**

- **Base de INSS:** R$ 15.560,00
- **Base de INSS do 13º salário:** R$ 5.700,00
- **Licença-maternidade total:** R$ 2.500,00, sendo:
  - **R$ 2.000,00** referentes à folha mensal;
  - **R$ 500,00** referentes ao 13º salário.

Para o cálculo da contribuição patronal, o sistema considera apenas a base de INSS da folha mensal e deduz somente o valor da licença-maternidade correspondente à folha mensal, desconsiderando os valores relacionados ao 13º salário.

Dessa forma, o cálculo é realizado da seguinte maneira:

**Base de cálculo:**

R$ 15.560,00 − R$ 2.000,00 = **R$ 13.560,00**

Aplicando a alíquota patronal de **10%** (conforme o Registro Fiscal):

**R$ 13.560,00 × 10% = R$ 1.356,00**

**Total da contribuição patronal (parte da empresa): R$ 1.356,00.**

### Como ajustar o valor no Resumo da Folha

Caso seja necessário ajustar a apresentação do valor no resumo, siga os passos abaixo:

**(1)** Acesse a tela **"Registro Fiscal"** (Pessoal Rotinas Registro Fiscal) da competência desejada.

**(2)** Localize a aba **"Desoneração"** e identifique se o campo está preenchido corretamente.

![Imagem 1: Verifique se, no cadastro da empresa, o campo " Indicativo de Desoneração da Folha " está marcado.](https://ajuda.sankhya.com.br/hc/article_attachments/41586004469143)

**(3)** Verifique se, no cadastro da empresa, o campo "**Indicativo de Desoneração da Folha**" está marcado.

![Imagem 2: Retorne ao "Resumo da Folha" e verifique se o valor foi ajustado conforme desejado.](https://ajuda.sankhya.com.br/hc/article_attachments/41585792925591)

**(4)** Retorne ao **"Resumo da Folha"** e verifique se o valor foi ajustado conforme desejado.

### Considerações sobre desoneração e 13º salário

Empresas que possuem **desoneração da folha de pagamento** devem estar atentas ao regime de transição estabelecido pela **Lei nº 12.546/2011**. Segundo essa legislação, o 13º salário pode ter tratamento diferenciado conforme o percentual de desoneração configurado.

Quando o 13º salário está configurado como **100% desonerado**, ele **não compõe o cálculo do INSS patronal**, sendo considerado apenas na base de cálculo da contribuição sobre a receita bruta.

Verifique sempre a **configuração do regime de desoneração** na tela de **"Registro Fiscal"** para garantir que os cálculos estejam de acordo com a legislação vigente e a situação específica da empresa.

Consulte também o artigo de [**Reoneração da folha de pagamento.**](https://ajuda.sankhya.com.br/hc/pt-br/articles/31031737058839-Reonera%C3%A7%C3%A3o-da-folha-de-pagamento)
