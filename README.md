
# Case de Engenharia de Dados



## Considerações importantes
 - O Postgres vai fazer a função do nosso banco OLAP para esse exercício;
 - No cenários real, pagamos tanto por armazenamento quanto por dando recuperado na query;
 - Mas o custo de query é muito mais elevado que o de armazenamento, então é um requisito minimizar o custo de query;
 - Os times de negócio consultando várias vezes ao dia os dados via dashboard, então geralmente query são exexcutadas com frequência;
 - Técnicas como particionamento e clusterização podem ser utilizadas para isso, mas não é o caso nesse case, o maior foco é organizar tabelas que permitam consultas inteligentes;
 - Documentação escrita é um fator importante, há muitas pessoas trabalhando em contextos diferentes todo o tempo, então dependemos fortemente de playbooks e docs para alinhar soluções.

## Carregando os dados raw
Nessa etapa vamos realizar a extração dos dados, para não precisar utilizar uma API, decide por deixar os dados prontos em JSON.

O dado bruto tem o seguinte formato:
```json
{
    "coupon": "1AM5250082",
    "date_time": "20/12/2023 06:45:00",
    "price_total": "40.00",
    "payments": [
    {
        "type": "Dinheiro",
        "amount": "40.00"
    }
    ],
    "timestamp_erp": 1703054700,
    "details": {
        "movimento": "",
        "operator": "00256",
        "abertura": "",
        "pdv": "14"
    },
    "fee": "4.29",
    "delivery": false,
    "staff": false,
    "items": [
        {
            "item": "Sanduíche Bauru",
            "canceled": "false",
            "total": "20.00",
            "price": "20.00",
            "quantity": 1
        }
    ]
}
```
A primeira etapa é subir o dado raw para o Postgres.
Utilize o método que quiser para resolver essa parte, pode ser um script em Python, pode ser uma aplicação. Aqui é a sua escolha como responsável pelo projeto.

Alguns requisitos:
 - Cupons que começam com 4 são atendimento de delivery
 - Cupons que começam com 3 são auto atendimento;
 - Cupons que começam com 1 são no restaurante

```
Deixei configurado na forma de docker-compose o Spark e o banco de dados Postgres, dessa forma podemos garantir a replicabilidade da aplicação.
```

## Transformando os dados do banco
Nessa etapa vamos usar o Spark para tranformar os dados, apesar de serem poucos e o Spark se tornar uma bazuca para o problema, o objetivo é simular uma situação onde haveriam diversos dados chegando.

Basicmamente, o ponto importante aqui é a utilização de uma ferramenta popular de pipeline da dados e a sua utilização.


### Checando se o spark está funcionado
Após subir o compose, entre dentro do container executando o comando a seguir:
```bash
sudo docker compose exec -it spark bash
```

Dentro do container, é possível executar o exemplo que deixei pronto, com o seguinte comando:
```bash
spark-submit  /opt/spark-apps/example.py
```

## Perguntas que o time de negócio geralmente quer responder
Finalmente, estamos muito interessados em ajudar o time de negócios a tirar insights dos dados extraídos, as perguntas que eles geralmente querem responder são as seguinte:

 - Qual o faturamento dessa loja em diferentes espaço de tempo: dia, semana e mês?
 - Quais os itens mais vendidos e menos vendidos? Quais itens trazem mais faturamento?
 - Quais os métodos de pagamento mais utilizado?
 - Quais os horários de maior movimento?
 - Quanto é a venda por modalidade: delivery, restaurante e auto atendimento?

Precisamos deixar possível a capacidade de responder as perguntas facilmente ao mesmo tempo que minimizamos a quantidade de dados que é recuperado em cada query.

Utilize a ferramenta de Data Viz que desejar, todas as possíveis devem ter compatibilidade com o Postgres. Adicione a ferramenta escolhida como um container de volta no docker-compose.yml de tal forma que eu possa executar na minha máquina localmente e visualizar os dashboards.

```
Os tipo de gráficos não são importantes, só quero ver o funcionamento das queries com relação a seletores de datas.
```

 ## Submissão e o que será avaliado
Se o repositório estiver privado, me adicione como contribuídor para que eu posso clonar. Seguirei a sua documentação para executar o projeto e olhar a visualização dos dados.

 ### Principais pontos de avaliação
 - A documentação que explica para outro desenvolvedor como executar o mesmo processo;
 - A forma como os dados foram transformados no pipeline;
 - Como as tabelas foram organizadas;
 - A documentação explicando o porquê da escolhas;
 - A documentação para o time de negócio de como eles podem utilizar as tabelas geradas.