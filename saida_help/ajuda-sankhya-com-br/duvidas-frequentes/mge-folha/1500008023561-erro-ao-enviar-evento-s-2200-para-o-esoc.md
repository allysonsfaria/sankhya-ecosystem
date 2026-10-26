---
id: "1500008023561"
titulo: "Erro ao enviar evento s-2200 para o eSocial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/1500008023561-Erro-ao-enviar-evento-s-2200-para-o-eSocial"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:31:18Z"
rotulos: ["Configuração", "Eventos", "Funcionários", "Nacionalidade", "#validadoRayssa", "#publicadoHyago", "eSocial", "E0101", "Campo país de nascimento ausente", "Preencha o país de nacionalidade corretamente", "Configurações incorretas de nacionalidade estrangeira", "Erro ao enviar evento s-2200 para o eSocial", "País Nacionalidade", "Erro"]
---

# Erro ao enviar evento s-2200 para o eSocial

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16336131839767) MENSAGEM**:

E0101 [eSocial/evtAdmissao/trabalhador/nascimento/paisNascto].

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16336131842071) SOLUÇÃO:**

Para a resolução do incidente:

![Imagem 3: Verifique se o campo País Nacionalidade está preenchido corretamente. (Arquivos » Funcionários » Aba Pessoais » campo…](https://ajuda.sankhya.com.br/hc/article_attachments/16336116856855) Verifique se o campo País Nacionalidade está preenchido corretamente. (Arquivos » Funcionários » Aba Pessoais » campo País Nacionalidade)

![Imagem 4: Verifique se o campo País Nacionalidade está preenchido corretamente. (Arquivos » Funcionários » Aba Pessoais » campo…](https://ajuda.sankhya.com.br/hc/article_attachments/15076730996503)

![Imagem 5: Acesse o MGE configurações e cadastre o país de acordo com a tabela 6 do eSocial, de acordo com o pais nacionalidade do…](https://ajuda.sankhya.com.br/hc/article_attachments/16336116860823) Acesse o MGE configurações e cadastre o país de acordo com a tabela 6 do eSocial, de acordo com o pais nacionalidade do funcionário. Deve ser criado uma cidade e uma UF, sendo que para a UF deve ser vinculada a sigla EX de exterior para que seja vinculado ao cadastro do funcionário.

![Imagem 6: Acesse o MGE configurações e cadastre o país de acordo com a tabela 6 do eSocial, de acordo com o pais nacionalidade do…](https://ajuda.sankhya.com.br/hc/article_attachments/15076806780695)

| MGE Configurações » Arquivos » Endereços » Países Clicar no '+' para cadastro do país.  MGE Configurações » Arquivos » Endereços » UF's Clicar no '+' para cadastro da UF e vincular o país cadastrado.  MGE Configurações » Arquivos » Endereços » Cidades Clicar no '+' para cadastro da cidade e vincular a UF na cidade cadastrada.    ![Imagem 7: MGE Configurações » Arquivos » Endereços » Países Clicar no '+' para cadastro do país. MGE Configurações » Arquivos »…](https://ajuda.sankhya.com.br/hc/article_attachments/42310187947671) |
| --- |

![Imagem 8: Gere novamente os eventos e realize o envio do evento.](https://ajuda.sankhya.com.br/hc/article_attachments/16336131845271) Gere novamente os eventos e realize o envio do evento.

**![Imagem 9: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16336131846167) CAUSA:**

Erro ocorre quando o funcionário tem a Nacionalidade estrangeira e o País Nacionalidade não está preenchido no cadastro ou as configurações do País estão incorretas.
