<?php
/**
 * Created by PhpStorm.
 * User: han
 * Date: 2016/3/11
 * Time: 15:38
 */

namespace App\Http\Controllers;


class MyController extends Controller{
    public static function subscribe()
    {
        $userId = Auth::user()->id;

    }
} 