from playwright.sync_api import sync_playwright

def test_login_and_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 1. Buka web
        page.goto("https://www.saucedemo.com")

        # 2. Isi form login
        page.fill('input[data-test="username"]', 'standard_user')
        page.fill('input[data-test="password"]', 'secret_sauce')
        page.click('input[data-test="login-button"]')

        # 3. Pastikan masuk halaman inventory
        assert "inventory.html" in page.url

        # 4. Klik Add to Cart
        page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')

        # 5. Cek cart badge muncul
        cart_count = page.locator('.shopping_cart_badge').inner_text()
        assert cart_count == "1"

        # 6. Buka keranjang
        page.click('.shopping_cart_link')

        # 7. Verifikasi isi keranjang
        item_name = page.locator('.inventory_item_name').inner_text()
        assert item_name == "Sauce Labs Backpack"

        if item_name == "Sauce Labs Backpack":
          print("✅ Test 1 selesai sukses!")
        else:
          print("❌ Test 1 selesai gagal!")

        browser.close()

def test_logout():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      page = browser.new_page()
        
      # 1. Buka web
      page.goto("https://www.saucedemo.com")

      # 2. Isi form login
      page.fill('input[data-test="username"]', 'standard_user')
      page.fill('input[data-test="password"]', 'secret_sauce')
      page.click('input[data-test="login-button"]')

      # 3. Pastikan masuk halaman inventory
      assert "inventory.html" in page.url

      # 4. Klik hamburger button lalu logout
      page.click('button#react-burger-menu-btn')
      page.wait_for_selector('a[data-test="logout-sidebar-link"]')
      page.click('a[data-test="logout-sidebar-link"]')

      # 5. Pastikan sudah terlogout
      assert "inventory.html" not in page.url
      homepage = "inventory.html"

      if homepage not in page.url:
        print("✅ Test 2 selesai sukses!")
      else:
        print("❌ Test 2 selesai gagal!")

      browser.close()

def checkout():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
        
    # 1. Buka web
    page.goto("https://www.saucedemo.com")

    # 2. Isi form login
    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')

    # 3. Pastikan masuk halaman inventory
    assert "inventory.html" in page.url

    # 4. Klik Add to Cart
    page.click('button[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('button[data-test="add-to-cart-sauce-labs-bike-light"]')

    # 5. Cek cart badge muncul
    cart_count = page.locator('.shopping_cart_badge').inner_text()
    assert cart_count == "2"

    # 6. Buka keranjang dan verify jumlah item
    page.click('.shopping_cart_link')
    item = page.locator('div[data-test="inventory-item"]')
    item_qty = item.count()
    assert item_qty == 2

    page.click('button[data-test="checkout"]')

    # 7. Isi data checkout
    page.fill('input[data-test="firstName"]', 'Nama')
    page.fill('input[data-test="lastName"]', 'Belakang')
    page.fill('input[data-test="postalCode"]', '11111')
    page.click('input[data-test="continue"]')

    # 8. Validasi total harga dan verifikasi subtotal
    harga_locator = page.locator('[data-test="inventory-item-price"]')
    subtotal_locator = page.locator('[data-test="subtotal-label"]').inner_text()
    count_harga = harga_locator.count()

    harga_list = []
    for i in range(count_harga):
      harga = harga_locator.nth(i).inner_text()
      harga_list.append(harga)

    harga_float = [float(h.replace('$', '')) for h in harga_list]
    subtotal = subtotal_locator.replace('Item total: $', '')
    total_harga = sum(harga_float)

    print("List harga:", harga_list)
    print("Total harga:", total_harga)
    print("Subtotal:", subtotal)

    # 9. Klik Finish
    page.click('button[data-test="finish"]')

    # 10. Verifikasi halaman selesai
    assert "checkout-complete.html" in page.url

    if float(subtotal) == total_harga:
        print("✅ Subtotal sesuai dengan total harga!")
    else:
        print("❌ Subtotal TIDAK sesuai dengan total harga!")

    # page.wait_for_timeout(3000)

    browser.close()

if __name__ == "__main__":
    test_login_and_add_to_cart()
    test_logout()
    checkout()