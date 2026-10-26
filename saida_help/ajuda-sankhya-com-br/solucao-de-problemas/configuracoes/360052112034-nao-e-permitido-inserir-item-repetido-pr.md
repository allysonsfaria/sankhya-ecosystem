---
id: "360052112034"
titulo: "Não é permitido inserir item repetido. Produto XXXX já existe na sequência X pelo executante X"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052112034-N%C3%A3o-%C3%A9-permitido-inserir-item-repetido-Produto-XXXX-j%C3%A1-existe-na-sequ%C3%AAncia-X-pelo-executante-X"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-07T18:52:47Z"
rotulos: ["#criadoroger", "Produtos", "Configuração", "TOP", "Preferências", "CORE_E04343", "Erro ao Inserir Item Repetido na NF-e", "Erro"]
---

# Não é permitido inserir item repetido. Produto XXXX já existe na sequência X pelo executante X

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18613212161687) MENSAGEM**:

[CORE\_E04343] Não é permitido inserir item repetido. Produto XXXX já existe na sequência X pelo executante X.

![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18613232298391) **CAUSA:**

Ocorre quando ou a TOP não permite esse tipo de lançamento e/ou os parâmetros informados acima não estão devidamente ligados para permitir lançar produto repetido na mesma nota/pedido.

**![Imagem 3: SOLUÇÃO: Acesse a tela 'Preferências' (Configurações » Avançado » Preferências);](https://ajuda.sankhya.com.br/hc/article_attachments/18613212188439) SOLUÇÃO:**
![Imagem 4: SOLUÇÃO: Acesse a tela 'Preferências' (Configurações » Avançado » Preferências);](https://ajuda.sankhya.com.br/hc/article_attachments/18613212195607) Acesse a tela 'Preferências' (Configurações » Avançado » Preferências);

Verifique os parâmetros abaixo, se LIGADOS eles permitem lançar produtos repetidos.

- **Aceitar prod.repetido para Exec.diferente?  - ACEITARPRODREPE**  [Ligado]
- **Aceitar produto repetido  - ACEITARPRODREP**                                  [Ligado]

![Imagem 5: Acesse a tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)](https://ajuda.sankhya.com.br/hc/article_attachments/18613232328983) Acesse a tela 'Tipos de Operação - TOP' (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)

- Aba validações
- Opção: **Aceitar Produto Repetido:**' [Sim ou Usar o Parâmetro Global] - Esta marcação é histórica, então se houver manutenção nesta opção, deverá lançar novamente o documento (Nota/pedido/Orçamento).

![Imagem 6: Após os ajustes refazer a nota, e será permitido lançar duas vezes o mesmo produto (sequências diferentes).](https://ajuda.sankhya.com.br/hc/article_attachments/18613212217367) Após os ajustes refazer a nota, e será permitido lançar duas vezes o mesmo produto (sequências diferentes).
