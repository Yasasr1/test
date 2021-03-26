import constants

CONFIG = {
    "basic": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "test/callback",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }
                ]
            }
        ],
        "override": {
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2_consent",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    },
    "implicit": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "test/callback",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }
                ]
            }
        ],
        "override": {
            "oidcc-ensure-request-with-valid-pkce-succeeds": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    },
    "hybrid": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "test/callback",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }
                ]
            }
        ],
        "override": {
            "oidcc-ensure-request-with-valid-pkce-succeeds": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2_consent",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    },
    "formpost-basic": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "oauth2/authorize",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify authorize",
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "optional": True,
                        "commands": [
                            [
                                "wait",
                                "xpath",
                                "/html/body/div/div/div/p/a",
                                10
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/div/div/div/p/a"
                            ]
                        ]
                    },
                    {
                        "task": "Verify callback",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }
                ]
            }
        ],
        "override": {
            "oidcc-prompt-none-not-logged-in": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback?error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-response-type-missing": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback?error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2_consent",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2/authorize",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2/authorize",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    },
    "formpost-implicit": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "authorize?sessionDataKey",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify authorize",
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "optional": True,
                        "commands": [
                            [
                                "wait",
                                "xpath",
                                "/html/body/div/div/div/p/a",
                                10
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/div/div/div/p/a"
                            ]
                        ]
                    },
                    {
                        "task": "Verify callback",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }

                ]
            }
        ],
        "override": {
            "oidcc-prompt-none-not-logged-in": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback#error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-response-type-missing": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback?error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "authorize?sessionDataKey",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-without-nonce-fails": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback#error_description*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "authorize?sessionDataKey",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "authorize?sessionDataKey",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    },
    "formpost-hybrid": {
        "browser": [
            {
                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                "tasks": [
                    {
                        "task": "Login",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                        "optional": True,
                        "commands": [
                            [
                                "text",
                                "id",
                                "usernameUserInput",
                                "admin"
                            ],
                            [
                                "text",
                                "id",
                                "password",
                                "admin"
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                            ],
                            [
                                "wait",
                                "contains",
                                "authorize?sessionDataKey",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Consent",
                        "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                        "optional": True,
                        "commands": [
                            [
                                "wait",
                                "id",
                                "approve",
                                10
                            ],
                            [
                                "click",
                                "id",
                                "approve"
                            ],
                            [
                                "wait",
                                "contains",
                                "test/callback",
                                10
                            ]
                        ]
                    },
                    {
                        "task": "Verify authorize",
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "optional": True,
                        "commands": [
                            [
                                "wait",
                                "xpath",
                                "/html/body/div/div/div/p/a",
                                10
                            ],
                            [
                                "click",
                                "xpath",
                                "/html/body/div/div/div/p/a"
                            ]
                        ]
                    },
                    {
                        "task": "Verify callback",
                        "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                    }
                ]
            }
        ],
        "override": {
            "oidcc-prompt-none-not-logged-in": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback#error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-response-type-missing": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback?error*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-refresh-token": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "oauth2_consent",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "test/callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-registered-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-without-nonce-fails": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error page",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-ensure-request-object-with-redirect-uri": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Verify error",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_error.do*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "//*",
                                        10,
                                        "Identity Server",
                                        "update-image-placeholder"
                                    ]
                                ]
                            }
                        ]
                    }
                ]
            },
            "oidcc-prompt-login": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "authorize?sessionDataKey",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            },
            "oidcc-max-age-1": {
                "browser": [
                    {
                        "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                        "tasks": [
                            {
                                "task": "Login",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/login*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/main/div/div[2]/h3",
                                        10,
                                        "Sign In",
                                        "update-image-placeholder-optional"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "usernameUserInput",
                                        "admin"
                                    ],
                                    [
                                        "text",
                                        "id",
                                        "password",
                                        "admin"
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/main/div/div[2]/div/form/div[9]/div[2]/button"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "authorize?sessionDataKey",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Consent",
                                "match": constants.IS_HOSTNAME + "/authenticationendpoint/oauth2_consent*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "id",
                                        "approve",
                                        10
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "rememberApproval",
                                        "optional"
                                    ],
                                    [
                                        "click",
                                        "id",
                                        "approve"
                                    ],
                                    [
                                        "wait",
                                        "contains",
                                        "callback",
                                        10
                                    ]
                                ]
                            },
                            {
                                "task": "Verify authorize",
                                "match": constants.IS_HOSTNAME + "/oauth2/authorize*",
                                "optional": True,
                                "commands": [
                                    [
                                        "wait",
                                        "xpath",
                                        "/html/body/div/div/div/p/a",
                                        10
                                    ],
                                    [
                                        "click",
                                        "xpath",
                                        "/html/body/div/div/div/p/a"
                                    ]
                                ]
                            },
                            {
                                "task": "Verify callback",
                                "match": "https://localhost.emobix.co.uk:8443/test/a/test/callback*"
                            }
                        ]
                    }
                ]
            }
        }
    }

}
