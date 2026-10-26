---
id: "360045094453"
titulo: "Melhores Práticas para configuração e geração do Bloco H (Inventário) no EFD-Fiscal."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045094453-Melhores-Pr%C3%A1ticas-para-configura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-do-Bloco-H-Invent%C3%A1rio-no-EFD-Fiscal"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:51:14Z"
rotulos: ["#RevisadoJR", "Configuração", "Inventário", "Fiscal", "EFD", "Estoque", "Preferências", "Bloco H: Inventário anual do estoque", "Configurações: Data custo e contas contábeis", "Rotinas: Gere e revise o Bloco H no EFD"]
---

# Melhores Práticas para configuração e geração do Bloco H (Inventário) no EFD-Fiscal.

O bloco H é o registro destinado ao preenchimento das informações do inventário, ou seja, estoque do contribuinte.

Geralmente (em caráter geral, salvo os casos de exceção e motivos de geração do mesmo) deve prestar contas ao Fisco referente ao estoque existente em 31 de dezembro no arquivo da EFD-ICMS/IPI da competência fevereiro. O chamado Bloco H da EFD-ICMS/IPI, deve ser preenchido e transmitido até o dia 'definido pelo estado do contribuinte/declarante do SPED no mês março'.

Fonte: [Guia Prático](http://sped.rfb.gov.br/estatico/AE/B0DEF8D93F24CB4EEFE8AD1443A14E7E8F4319/GUIA%20PR%C3%81TICO%20EFD%20ICMS%20IPI%20-%20Vers%C3%A3o%203.01.pdf)

- **Composição do Bloco H**

**H001** Abertura do Bloco H
**H005** Totais do Inventário
**H010** Inventário
**H020** Informação complementar do Inventário
**H990** Encerramento do Bloco H

- **Configurações para gerar o bloco H no EFD ICMS/IPI**

É premissa que tenha registro na rotina de Cópia/Contagem de Estoque, o processo de Inventario usualmente é feito ate o final do ano anterior, mas podendo ficar  a escolha da empresa efetuar a contagem em qual data desejar.

![Imagem 1: Rotinas usadas para Copia e Contagem de Estoque](https://ajuda.sankhya.com.br/hc/article_attachments/19196859830807) Rotinas usadas para Copia e Contagem de Estoque

- 1.1-[Inventário » Arquivo » Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514)
- 1.2-[Inventário » Arquivo » Contagem de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609694)

![Imagem 2: Comercial » Preferências » Empresa](https://ajuda.sankhya.com.br/hc/article_attachments/19196830534679) Comercial » Preferências » Empresa

Efetuar a configuração dos Blocos e Registros do EFD Fiscal, nas Preferencias da Empresa, para que seja gerado o BLOCO H

![Imagem 3: Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI](https://ajuda.sankhya.com.br/hc/article_attachments/19196830542999) Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI

Ao gerar o EFD-ICMS/IPI da competência Fevereiro, é necessário preencher o campo 'Data do Inventario'. Com a possível escolha entre a Data da Cópia ou a Data da Contagem.

![Imagem 4: Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI aba: Opções](https://ajuda.sankhya.com.br/hc/article_attachments/19196830545175) Livros Fiscais » Conexão » EFD - Escrituração Fiscal Digital - ICMS/IPI aba: Opções

Ao preencher a 'Data do Inventario' na geração do arquivo EFD, se faz necessário a escolha do Custo a ser considerado na geração do Bloco H-Verificar o custo conforme instruções da Contabilidade.

- **Configuração para geração das Contas Contábeis no Registro H010**

![Imagem 5: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/19196859847703) Configurações » Avançado » Preferências

Parâmetro **Conta p/inventário (H010) do EFD (SPED FISCAL) - EFDH010**

5.1- Pode ser configurado o parâmetro EFDH010-Conta p/inventário (H010) do EFD (SPED FISCAL) **para uso Global.**

Deverá ser informado neste parâmetro o nome ou a própria conta contábil que a Empresa utiliza para os estoques, se a conta contábil 1,2,3 ou 4 da aba Impostos da seguinte forma:

- Parâmetro **EFDH010** = CONTAPRODUTO1
  O sistema busca a conta contábil 1 do Cadastro de Produtos (TGFPRO.CODCTACTB);
- Parâmetro **EFDH010** = CONTAPRODUTO2
  O sistema busca a conta contábil 2 do Cadastro de Produtos (TGFPRO.CODCTACTB2);
- Parâmetro **EFDH010** = CONTAPRODUTO3
  O sistema busca a conta contábil 3 do Cadastro de Produtos (TGFPRO.CODCTACTB3);
- Parâmetro **EFDH010** = CONTAPRODUTO4
  O sistema busca a conta contábil 4 do Cadastro de Produtos (TGFPRO.CODCTACTB4).

Desta forma, no momento da geração do SPED FISCAL no registro H010, campo 10-COD\_CTA o sistema saberá qual conta informada no produto deverá usar para o estoque se a CONTAPRODUTO1, CONTAPRODUTO2, CONTAPRODUTO3 ou CONTAPRODUTO4.

Também podemos ter mais duas variações:

Se EFDH010 = "1.1.05.04.0001" (exemplo) a própria conta ele vai usar esta para geração (Obs. tem que ser uma conta válida e existente no plano de contas).

Se EFDH010 = "" (vazio) não sera gerada nenhuma informação da conta no H010.""

5.2- Ou, pode ser configurado a Conta **contábil por empresa**, através da rotina:

Comercial » Preferências » Empresa, aba: EFD-Escrituração Fiscal Digital.
Tipo de Escrituração: EFD
Sub-aba: Geração do registro H010.
Campo: **'Conta p/ inventario (H010) do EFD.**

Detalhes a respeito das contas contábeis correspondentes ao registro H010 podem ser visualizados por meio do artigo  [Geração da Conta Contábil para o registro H010](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607614#geraodacontacontbilparaoregistroh010)

- **Vejamos o Bloco e Registro H, gerado no arquivo txt da EFD.**

|H001|0|
|H005|31122018|89420,55|01|
|H010|1|UN|9998,000|0,000000|0,00|0||dfgd|1.1.4.10.001|0,00|
|H020|000|0,00|0,00|
|H990|1|
