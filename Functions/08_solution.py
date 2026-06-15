def key_values_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
key_values_function(name = "Koustav", Skill = "Automation")
key_values_function(name = "Koustav")
key_values_function(name = "Koustav", Skill = "Automation", learning = "AI in Testimg")
