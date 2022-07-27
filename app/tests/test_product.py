from fastapi.testclient import TestClient

def test_product_create(client: TestClient, category_factory, supplier_factory, admin_auth_header):
    category = category_factory()
    supplier = supplier_factory()

    response = client.post('/product/', headers=admin_auth_header,
                           json={
                               'description': 'texto',
                               'price': 10,
                               'image': 'rotas de imagens',
                               'technical_details': 'qualquer coisa',
                               'visible': True,
                               'category_id': category.id,
                               'supplier_id': supplier.id
                           })

    assert response.status_code == 201
    assert response.json()['description'] == 'text'
    assert response.json()['category_id'] == category.id
    assert response.json()['supplier_id'] == supplier.id



def test_product_show(client: TestClient, category_factory, supplier_factory, admin_auth_header):
    category = category_factory()
    supplier = supplier_factory()
    for i in range(1,4):
        client.post('/product/', headers=admin_auth_header,
                            json={
                                'description': f'descricao {i-1}',
                                'price': 10,
                                'image': 'image.dev',
                                'technical_details': f'qualquer coisa {i-1}',
                                'visible': True,
                                'category_id': category.id,
                                'supplier_id': supplier.id
                            })
    for i in range(1,4):
        response = client.get(f'/product/{i}', headers=admin_auth_header)
        assert response.status_code == 200
        assert response.json()['description'] == f'text {i-1}'
        assert response.json()['technical_details'] == f'qualquer coisa {i-1}'
        assert response.json()['category_id'] == category.id
        assert response.json()['supplier_id'] == supplier.id