from neo4j.v1 import GraphDatabase, basic_auth
driver11 = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "admin123"))
session11 = driver11.session()
session11.run("CREATE (a:Person {name:'Rahul',title:'Mod'})")
result11= session11.run("MATCH (a:Person) WHERE a.name ='Rahul' RETURN a.name AS name, a.title AS title")
for record in result11:
    print("%s %s"% (record["title"], record["name"]))
session11.close()