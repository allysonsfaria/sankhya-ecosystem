---
id: "360044110834"
titulo: "O campo é obrigatório para EFD ICMS/IPI com Perfil igual a 'A' ou 'B\". Campo: 10-COD_CTA. Registro: H010"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044110834-O-campo-%C3%A9-obrigat%C3%B3rio-para-EFD-ICMS-IPI-com-Perfil-igual-a-A-ou-B-Campo-10-COD-CTA-Registro-H010"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:53:00Z"
rotulos: ["#RevisadoJR", "Configuração", "Contas", "Impostos", "EFD", "Estoque", "Gere o arquivo SPED e valide no PVA após ajustes.", "Campo 10-COD_CTA é obrigatório para EFD ICMS/IPI Perfil 'A' ou 'B", "Configure parâmetro EFDH010 com conta contábil ou valor específico", "SPED Fiscal"]
---

# O campo é obrigatório para EFD ICMS/IPI com Perfil igual a 'A' ou 'B". Campo: 10-COD_CTA. Registro: H010

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16783158111895) MENSAGEM:**

O campo é obrigatório para EFD ICMS/IPI com Perfil igual a 'A' ou 'B".

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16783158114711) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/16783168154135) Acesse: Configurações » Avançado » Preferências

- Parâmetro: **"EFDH010-Conta p/inventário (H010) do EFD (SPED FISCAL)"**
- Pode ser configurado o parâmetro EFDH010-Conta p/inventário (H010) do EFD (SPED FISCAL) para uso Global.

**(1)** Informe neste parâmetro o nome ou a própria conta contábil que a Empresa utiliza para os estoques, se a conta contábil 1,2,3 ou 4, da aba **"Impostos"** da seguinte forma:

- Parâmetro EFDH010 = CONTAPRODUTO1 -> o sistema busca a conta contábil 1 do Cadastro de Produtos (TGFPRO.CODCTACTB);
- Parâmetro EFDH010 = CONTAPRODUTO2 -> o sistema busca a conta contábil 2 do Cadastro de Produtos (TGFPRO.CODCTACTB2);
- Parâmetro EFDH010 = CONTAPRODUTO3 -> o sistema busca a conta contábil 3 do Cadastro de Produtos (TGFPRO.CODCTACTB3);
- Parâmetro EFDH010 = CONTAPRODUTO4 -> o sistema busca a conta contábil 4 do Cadastro de Produtos (TGFPRO.CODCTACTB4).

![Imagem 4: Desta forma, no momento da geração do SPED FISCAL no registro H010, campo 10-COD_CTA o sistema saberá qual conta…](https://ajuda.sankhya.com.br/hc/article_attachments/16783158118679) Desta forma, no momento da geração do SPED FISCAL no registro H010, campo 10-COD\_CTA o sistema saberá qual conta informada no produto deverá usar para o estoque se a CONTAPRODUTO1, CONTAPRODUTO2, CONTAPRODUTO3 ou CONTAPRODUTO4.

**(1)** Também pode-se ter mais duas variações:

- Se EFDH010 = "1.1.05.04.0001" (exemplo) a própria conta ele vai usar esta para geração (**Observação:** tem que ser uma conta válida e existente no plano de contas).
- Se EFDH010 = "" (vazio) não será gerada nenhuma informação da conta no H010.""

![Imagem 5: Ou pode ser configurado a Conta contábil por empresa , através da rotina:](https://ajuda.sankhya.com.br/hc/article_attachments/16783168163607) Ou pode ser configurado a **Conta** **contábil por empresa**, através da rotina:

- Comercial » Preferências » Empresa, aba: EFD-Escrituração Fiscal Digital:
  Tipo de Escrituração: EFD
  Sub-aba: **"Geração do registro H010"**.
  Campo: **"Conta p/ inventario (H010) do EFD"**

![Imagem 6: Após os ajustes, gere novamente um novo arquivo do SPED e valide no PVA.](https://ajuda.sankhya.com.br/hc/article_attachments/16783158128023) Após os ajustes, gere novamente um novo arquivo do SPED e valide no PVA.

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16783168171287) CAUSA:**

De acordo com a legislação da Receita, para o SPED de Fevereiro, se faz necessário a apresentação do bloco H de forma obrigatória, referente ao Inventario criado ate 31 de Dezembro do ano anterior. Desta forma, se faz necessária a apresentação da Conta Contábil dos produtos relacionados no bloco H para os perfis A e B.
