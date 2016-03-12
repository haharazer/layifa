<?php
/***************************************************************************
 *
 * Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
 *
 **************************************************************************/

/**
 * @file HomeController.php
 * @author hanpeng03(@baidu.com)
 * @date 15/8/14 下午10:56
 * @brief
 *
 **/

namespace App\Http\Controllers;

use DB;

class HomeController extends Controller
{
    public static function index()
    {
        $items = DB::table('discounts')
            ->orderBy('created_at', 'desc')
            ->paginate(12);

        return view('home', ['title' => '主页', 'items'=> $items]);
    }
}